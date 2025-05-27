import tweepy


# EAB0oskrfQ0HS-yCITtkVJgHrZuVmvyB2rhrp3DXkfCHlzX02K
API_KEY = "meKodhPeJfEmu9rQu1fE0va7L"
API_KEY_SECRET = "pJibI7VkietgkhT2o2EdpjA7d6xz0mF2Bk9TbULqxWIr4rD0RX"
ACCESS_TOKEN = "1925977787845787648-qqgrhVSaRhoc21hm4Ip1QRAPDokquP"
ACCESS_TOKEN_SECRET = "goHNsiV4hIA78NCFq1uLrokHbABBzkYy4qE3AhDyHrTCd"


client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET)


# Image/media upload is not available with Tweepy v2 for Free accounts.
def post_tweet(text, image_path=None):
    """
    Posts a tweet (text only) using Tweepy v2.
    Image support is not available for v2 with Free tier.
    """
    try:
        client.create_tweet(text=text)
        print("Tweet posted successfully!")
    except Exception as e:
        print(f"Failed to post tweet: {e}")
