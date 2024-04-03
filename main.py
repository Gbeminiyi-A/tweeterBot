import tweepy
import requests
import os
from dotenv import load_dotenv

load_dotenv()


CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_sECRET']

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

API_KEY = os.environ['API_KEY']
API_SECRET_KEY = os.environ['API_SECRET_KEY']

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,)

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
)

response = requests.get('https://africanproverbs.onrender.com/api/proverb')
response = response.json()

text = (f"{response['proverb'].title()}\n\n~ {response['native'].title()}\nSource: https://africanproverbs"
        f".onrender.com/api/proverb")

if __name__ == "__main__":
    client.create_tweet(text=text, user_auth=True)
