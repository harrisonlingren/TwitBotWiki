import tweepy, json
from getTwitterAuth import getTwitterAuth
from MyStreamListener import MyStreamListener


auth = getTwitterAuth()
api = tweepy.API(auth)
	
myStreamL = MyStreamListener()
myStream = tweepy.Stream(auth, myStreamL)	
myStream.filter(track=['BotForWiki'])