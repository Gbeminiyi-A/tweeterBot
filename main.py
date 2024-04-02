import tweepy
import requests


CLIENT_ID = "SVUwTmh5ZW1xNzRyT1ljQWdQSTc6MTpjaQ"
CLIENT_SECRET = "EPa54O3JtPWv43zeFnANYsjIpIRxorcd43-F5dOTxB6H5inxX4"

ACCESS_TOKEN = "1775222552576622592-oRScR58GN3S2k0hSNkSwl7Vy1fu1vJ"
ACCESS_TOKEN_SECRET = "mKn954XKBU915DjiKfX1a2rV2dB4nmuycvx60GDnSWPhH"

API_KEY = "ytdeI9s3YkU3o607pDd0fJluc"
API_SCERET_KEY = "gqjWn0ICFOLkprKWSMacYZWb0zlkMxJbXPb9JJMvPqUyyGBSQV"

auth = tweepy.OAuthHandler(API_KEY, API_SCERET_KEY)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,)

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SCERET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
)

response = requests.get('https://africanproverbs.onrender.com/api/proverb')
response = response.json()

text = f"Proverb: {response['proverb'].title()}\nOrigin: {response['native'].title()}"

if __name__ == "__main__":
    client.create_tweet(text=text, user_auth=True)
