import tweepy



CONSUMER_KEY = "CONSUMER_KEY"
CONSUMER_SECRET = "CONSUMER_SECRET"
ACCESS_TOKEN = "ACCESS_TOKEN"
ACCESS_SECRET = "ACCESS_SECRET"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


tweets = api.user_timeline(id = "id")

for status in tweets:
    if ((not status.retweeted) and ("RT @" not in status.text)) and ("@" not in status.text):
        tweet_id = status.id
        try:
            api.retweet(tweet_id)
        except Exception as e:
            print(e)
