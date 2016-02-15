import tweepy, json, wikipedia, re, unicodedata
from getTwitterAuth import getTwitterAuth
from pyshorteners import Shortener

def TwitBotWiki(tweet):
	
	auth = getTwitterAuth()
	api = tweepy.API(auth)
	
	parsedJSON = json.loads(tweet)
	
	tweet_user = parsedJSON['user']['screen_name']
	tweet_id = parsedJSON['id_str']
	tweet_text = parsedJSON['text']
	
	term = re.findall('"([^"]*)"', tweet_text)
	print('>  @'+tweet_user+': '+tweet_text+' | term: '+term[0])
	
	reply = ('@' + tweet_user + wikiToString(term))
	replyASCII = str(unicodedata.normalize('NFKD', reply).encode('ascii','ignore'))
	
	print("  >  " + replyASCII,'\n')
	
	api.update_status(reply, in_reply_to_status_id = tweet_id)
	return 'Tweet Sent!'
	
def wikiToString(term):
	
	wikiPage = wikipedia.page(wikipedia.search(term)[0])
	wikiURL = shortURL(wikiPage.url)
	wikiSummary = wikiPage.summary
	summ = (wikiSummary[0:79])
	
	outp = (' ' + summ + '... Read more: ' + wikiURL)
	
	return outp
	
def shortURL(url):
	shortener = Shortener('IsgdShortener')
	return "{}".format(shortener.short(url))