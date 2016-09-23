from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
from senti.sentiment import *
from pubnub import Pubnub
import simplejson as json
from threading import Timer
import time


pubnub = Pubnub(publish_key="PUBLISH_KEY", subscribe_key="SUBSCRIBE_KEY")

totaltweetcount = 0
sentimentvalue = 0
tweetcounter = 0
average = 0
tweetdata = ''
# pubnub code here
def callback(message, channel):
    print(message)

def averageSenti(incomingData, tweet):
    '''
    calculate average sentiment per second to get a smooth sentiment stream
    :param incomingData:
    :return:
    '''
    global sentimentvalue
    global tweetcounter
    global average
    global tweetdata
    tweetdata = tweet
    tweetcounter += 1
    sentimentvalue += incomingData
    average = sentimentvalue/tweetcounter

def pub():
    '''
    Method to publish the average sentiments per second
    :return:
    '''
    global sentimentvalue
    global tweetcounter
    global average
    global tweetdata
    global totaltweetcount
    print(average)

    msg = {'data3':average, 'tweet':tweetdata, 'count':totaltweetcount}
    average = 0
    sentimentvalue = 0
    tweetcounter = 0

    data2 = json.dumps(msg)
    pubnub.publish(channel='c3-bar', message=data2)
    Timer(1, pub).start()

def error(message):
    print("ERROR : " + str(message))


def connect():
    print("CONNECTED")

def reconnect(message):
    print("RECONNECTED")


def disconnect(message):
    print("DISCONNECTED")


#twitter streaming code

consumer_key =  "consumer key"
consumer_secret = "consumer secret"
access_token = "access token"
access_token_secret = "access token secret"

#authorize
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
        global totaltweetcount
        sentiment, tweet = sentimentAnalysis(data)
        totaltweetcount = totaltweetcount + 1
        print(tweet)
        averageSenti(sentiment,tweet)
        return True

    def on_error(self, status):
        print(status)
