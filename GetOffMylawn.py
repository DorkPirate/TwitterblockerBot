import tweepy
import time

# Replace these with your API keys
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def block_new_followers():
    print("Starting to block new followers...")
    my_id = api.me().id
    followers = api.followers_ids(my_id)
    for follower in followers:
        try:
            print(f"Blocking user with ID {follower}")
            api.create_block(user_id=follower)
        except tweepy.TweepError as e:
            print(f"Error blocking user {follower}: {e}")

if __name__ == "__main__":
    while True:
        block_new_followers()
        print("Sleeping for 60 seconds...")
        time.sleep(60)