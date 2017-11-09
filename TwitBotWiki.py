import tweepy, json, wikipedia, re, unicodedata, requests
from getTwitterAuth import getTwitterAuth

def TwitBotWiki(tweet):
	
	auth = getTwitterAuth()
	api = tweepy.API(auth)
	
	parsedJSON = json.loads(tweet)
	tweet_user = parsedJSON['user']['screen_name']
	tweet_id = parsedJSON['id_str']
	tweet_text = parsedJSON['text']
	
	try:
		term = re.findall('"([^"]*)"', tweet_text)
		print('>  @'+tweet_user+': '+tweet_text+' | term: '+term[0])
		
		l = 239 - len(tweet_user) - 1
		reply = ('@' + tweet_user + wikiToString(term[0], l))
		replyASCII = str(unicodedata.normalize('NFKD', reply).encode('ascii','ignore'))
	except IndexError:
		print('>  @'+tweet_user+': '+tweet_text+' | IndexError, no term found')
		reply = ('@' + tweet_user + ' could not find "'+term[0]+'"! Try again.')
		replyASCII = str(unicodedata.normalize('NFKD', reply).encode('ascii','ignore'))
		pass
	
	print("  >  " + replyASCII,'\n')
	api.update_status(reply, in_reply_to_status_id = tweet_id)
	return 'Tweet Sent!'
	
	
def wikiToString(term, length):
	try:
		wikiPage = wikipedia.page(wikipedia.search(term)[0])
		wikiURL = shortURL(wikiPage.url)
		wikiSummary = wikiPage.summary
		summ = (wikiSummary[0:length])
		outp = (' ' + summ + '... Read more: ' + wikiURL)
	except wikipedia.exceptions.DisambiguationError:
		outp = ' Wiki article for "'+term+'" is a disambiguation! Try being more specific.'
		pass
		
	return outp
	
def shortURL(url):
	#shortener = Shortener('IsgdShortener')
	#return "{}".format(shortener.short(url))

	r = requests.post('https://fastl.ink/api/new', data=json.dumps( {'url': url} ))
	return r.text
