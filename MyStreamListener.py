import tweepy
from TwitBotWiki import TwitBotWiki

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
	def on_data(self, data):
		print(TwitBotWiki(data))
