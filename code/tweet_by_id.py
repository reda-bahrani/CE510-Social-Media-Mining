import tweepy
import pandas as pd

from codes import consumer_key, consumer_secret, access_token, access_token_secret

data = pd.read_csv("sample.tsv", sep="\t", names=["tweet_id", "date", "time", "language", "region"])

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet = api.get_status("1219343794845425672")
print(tweet._json)
