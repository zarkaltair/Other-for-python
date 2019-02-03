import tweepy

from textblob import TextBlob


# Create our app on apps.twitter.com and enter password and token
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


# Auth our app
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Search tweets
public_tweets = api.search('Tim Cook')
for tweet in public_tweets:

    # Print tweets
    print(tweet.text)

    # Use textblob for define key tweet

    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print('\n')