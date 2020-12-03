import tweepy



CONSUMER_KEY = "zfAnk9Uz9bEOhhvOWZw0jPOzv"
CONSUMER_SECRET = "MAl36eU4AsdBupiGUP11KIvT4yGEQgrO4bEXekvqh4U5koenoO"
ACCESS_TOKEN = "1334325540556132354-68zZdUJKJvjEjii8Lz8tgk79Lx4JfL"
ACCESS_SECRET = "OxueSL7rN7nAz78gq9qPCnpbdWU6Ze0mUTLJBgGpl73am"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


tweets = api.user_timeline(id = "printemps_317")

for status in tweets:
    if ((not status.retweeted) and ("RT @" not in status.text)) and ("@" not in status.text):
        tweet_id = status.id
        try:
            api.retweet(tweet_id)
        except Exception as e:
            print(e)
