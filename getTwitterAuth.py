import tweepy

def getTwitterAuth():

        auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
        auth.access_token = 'access_token'
        auth.access_token_secret = 'access_token_secret'
        return auth
