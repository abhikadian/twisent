from django.shortcuts import render
from django.http import HttpResponse
from senti.streaming import *
from .forms import SearchForm
from senti.streaming import *

# Create your views here.

consumer_key = "l9bg0dKzXFt02YW0DzrzJpZo7"
consumer_secret = "awBIisQwdB2Y8fw2c4tm701vI1rMDSJFLQzQUt6B3WYgxYVXmr"
access_token = "3268845463-bI3MPXRS7mX1nuhY2T7kVv3mVzpTe2shtbiePqj"
access_token_secret = "a6nvbn0UTFcMlixsFbgLVux8UVOFEchSgnS7qo0nFY83z"


# def index(request):
#     public_tweets = api.home_timeline()
#     data = ""
#     for tweet in public_tweets:
#         data = data +tweet.text
#     return HttpResponse(data)



# index page
def index(request):
    ''' Landing page for the website. Option to search twitter for a keyword

    :param request:
    :return:
    '''
    return render(request, 'senti/search.html')


#update the tweets
def update_tweets(request):
    return render(request, 'senti/update.html')



#home page
def home(request):
    '''
    Home page. process the get request, search twitter stream for that keyword.
    Uses streaming.py and sentiment.py files for sentiment analysis of the keywords
    :param request:
    :return:
    '''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    trends1 = api.trends_place(23424977)
    data = trends1[0]
    #     # # grab the trends
    trends = data['trends']



    if request.GET.get('search'):
        search = request.GET.get('search')

        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        stream = Stream(auth, l)
        connect()
        pub()
        stream.filter(track=[search])
        return render(request,'senti/home.html', {'trends': trends})
    else:
        return render(request, 'senti/home.html', {'trends': trends})
    '''else:
        return render(request, 'senti/home.html')
    '''


def searchKeyword(request):
    if request.GET.get('search'):
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        stream = Stream(auth, l)
        connect()
        pub()
        stream.filter(track=['iphone'])

        return HttpResponse("abcd")


def get_request(request):
    '''
    get request for processing the forms
    :param request:
    :return:
    '''
    form = SearchForm()
    return render(request, 'senti/home.html', {'form':form})