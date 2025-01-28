import os
import requests
from requests_oauthlib import OAuth1

# Load credentials from text files
current_dir = os.path.dirname(__file__)
api_key_path = os.path.join(current_dir, "api_key.txt")
api_secret_path = os.path.join(current_dir, "api_secret.txt")
access_token_path = os.path.join(current_dir, "access_token.txt")
access_secret_path = os.path.join(current_dir, "access_secret.txt")

with open(api_key_path, "r") as file:
    API_KEY = file.read().strip()
with open(api_secret_path, "r") as file:
    API_SECRET = file.read().strip()
with open(access_token_path, "r") as file:
    ACCESS_TOKEN = file.read().strip()
with open(access_secret_path, "r") as file:
    ACCESS_SECRET = file.read().strip()

# Use the correct Tweet ID from the provided link
TWEET_ID = "1883195857237062111"

# Twitter API endpoint to fetch a tweet
url = f"https://api.twitter.com/2/tweets/{TWEET_ID}?tweet.fields=created_at,author_id"

# Authenticate using OAuth 1.0a
auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
response = requests.get(url, auth=auth)
tweet_data = response.json()

# Check response and print results
if "data" in tweet_data:
    print("✅ Tweet fetched successfully!")
    print(f"Tweet ID: {tweet_data['data']['id']}")
    print(f"Text: {tweet_data['data']['text']}")
    print(f"Author ID: {tweet_data['data']['author_id']}")
    print(f"Created At: {tweet_data['data']['created_at']}")
else:
    print("❌ Failed to fetch tweet. Error:", tweet_data)
