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

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if ((not status.retweeted) and ("RT @" not in status.text)) and ("@" not in status.text):
                try:
                    tweet_id = status.id
                    api.retweet(tweet_id)
                except Exception as e:
                    print(e)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(follow = users)
