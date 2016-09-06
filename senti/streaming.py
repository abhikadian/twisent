from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
from senti.sentiment import *

consumer_key =  "l9bg0dKzXFt02YW0DzrzJpZo7"
consumer_secret = "awBIisQwdB2Y8fw2c4tm701vI1rMDSJFLQzQUt6B3WYgxYVXmr"
access_token = "3268845463-bI3MPXRS7mX1nuhY2T7kVv3mVzpTe2shtbiePqj"
access_token_secret = "a6nvbn0UTFcMlixsFbgLVux8UVOFEchSgnS7qo0nFY83z"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def getAPI():
	api = tweepy.API(auth)
	print("DEBUG: " + api.me().name + " is no logged in!")
	return api

def getAuth():
    return auth

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        sentimentAnalysis(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['basketball'])