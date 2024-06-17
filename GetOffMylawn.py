import tweepy
import time

# Replace these with your API keys
CONSUMER_KEY = '___'
CONSUMER_SECRET = '___'
ACCESS_TOKEN = '___'
ACCESS_TOKEN_SECRET = '___'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def block_new_followers():
    print("Starting to block new followers...")
    try:
        my_id = api.verify_credentials().id
    except tweepy.errors.TweepyException as e:
        print(f"Error verifying credentials: {e}")
        return

    try:
        followers = api.get_follower_ids(user_id=my_id)
    except tweepy.errors.Forbidden as e:
        print(f"Error getting followers (Forbidden): {e}")
        return
    except tweepy.errors.TweepyException as e:
        print(f"Error getting followers: {e}")
        return

    for follower_id in followers:
        try:
            follower = api.get_user(user_id=follower_id)  # Fetching user details
            print(f"Blocking user {follower.screen_name} with ID {follower_id}")
            api.create_block(user_id=follower_id)
        except tweepy.errors.Forbidden as e:
            print(f"Error blocking user (Forbidden): {e}")
        except tweepy.errors.TweepyException as e:
            print(f"Error blocking user: {e}")

if __name__ == "__main__":
    while True:
        block_new_followers()
        print("Sleeping for 60 seconds...")
        time.sleep(60)
