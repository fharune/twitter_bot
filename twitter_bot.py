import tweepy
import time
import config


CONSUMER_KEY = config.API_KEY
CONSUMER_SECRET = config.API_SECRET_KEY
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_SECRET = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)



class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if "@" not in status.text:
                try:
                    tweet_id = status.id
                    api.retweet(tweet_id)
                except Exception as e:
                    print(e)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(follow = config.users)
