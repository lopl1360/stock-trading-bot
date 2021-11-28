import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import credentials as cred


class TwitterClient(object):
	'''
	Generic Twitter Class for sentiment analysis.
	'''
	def __init__(self):
		'''
		Class constructor or initialization method.
		'''
		# keys and tokens from the Twitter Dev Console
		consumer_key = cred.TWITTER_API_KEY
		consumer_secret = cred.TWITTER_API_KEY_SECRET
		access_token = cred.TWITTER_ACCESS_TOKEN
		access_token_secret = cred.TWITTER_ACCESS_TOKEN_SECRET

		# attempt authentication
		try:
			# create OAuthHandler object
			self.auth = OAuthHandler(consumer_key, consumer_secret)
			# set access token and secret
			self.auth.set_access_token(access_token, access_token_secret)
			# create tweepy API object to fetch tweets
			self.api = tweepy.API(self.auth)
		except:
			print("Error: Authentication Failed")

	def get_tweets(self, query, count = 10):
		'''
		Main function to fetch tweets and parse them.
		'''
		# empty list to store parsed tweets
		tweets = []

		try:
			# call twitter api to fetch tweets
			fetched_tweets = self.api.search_tweets(q = query, count = count)
			# parsing tweets one by one
			for tweet in fetched_tweets:
				if tweet.text not in tweets:
						tweets.append(tweet.text)
			# return parsed tweets
			return tweets

		except tweepy.TweepError as e:
			# print error (if any)
			print("Error : " + str(e))