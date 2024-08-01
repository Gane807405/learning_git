import pandas as pd
import aiohttp
import asyncio

# Load the Excel file
excel_file_path = r'D:\ganesh\fake_followers_api\jj\rest_users.xlsx'
df = pd.read_excel(excel_file_path)

# API endpoint
api_url = 'https://pred.kofluence.com/ml/prediction/v1/fake-followers/users/'

# Function to make asynchronous API requests and get fake follower percentage
async def fetch_fake_percentage(session, username):
    if username:
        url = f'{api_url}{username}'
        try:
            async with session.get(url):
                # Do nothing with the response
                pass
        except Exception as e:
            print(e)
            pass

# Function to handle batched API requests
async def fetch_batch(session, usernames):
    tasks = [fetch_fake_percentage(session, username.strip()) for username in usernames]
    await asyncio.gather(*tasks)

# Process in batches of 4
batch_size = 4
async def main():
    usernames = df['usernames'].tolist()
    print(usernames[:10])
    print("Total usernames:", len(usernames))
    async with aiohttp.ClientSession() as session:
        for i in range(0, len(usernames), batch_size):
            batch_usernames = usernames[i:i + batch_size]
            await fetch_batch(session, batch_usernames)
            batch_num = (i // batch_size) + 1
            print(f"Completed batch {batch_num}")
            print("hello ")

if __name__ == '__main__':
    asyncio.run(main())
