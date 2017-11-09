import tweepy, os

def getTwitterAuth():
        c_k = os.environ.get('consumer_key')
        c_s = os.environ.get('consumer_secret')
        a_t = os.environ.get('access_token')
        a_t_s = os.environ.get('access_token_secret')

        auth = tweepy.OAuthHandler(c_k, c_s)
        auth.access_token = a_t
        auth.access_token_secret = a_t_s
        return auth
