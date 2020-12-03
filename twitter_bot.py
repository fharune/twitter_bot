import tweepy
import time


CONSUMER_KEY = "CONSUMER_KEY"
CONSUMER_SECRET = "CONSUMER_SECRET"
ACCESS_TOKEN = "ACCESS_TOKEN"
ACCESS_SECRET = "ACCESS_SECRET"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


users = ["id1", "id2"]

def get_timeline(name,since_id):
    for status in api.user_timeline(id = name, since_id = 1329902993420873729):
        if ((not status.retweeted) and ("RT @" not in status.text)) and ("@" not in status.text):
                tweet_id = status.id
                try:
                    api.retweet(tweet_id)
                except Exception as e:
                    print(e)
                    
for i, user in enumerate(users):
    get_timeline(user,i)


if __name__ == '__main__':
    while True:
        time.sleep(20)
        get_timeline(users,1329902993420873729)
