from django.shortcuts import render
from django.http import HttpResponse
from senti.streaming import *
# Create your views here.

# def index(request):
#     public_tweets = api.home_timeline()
#     data = ""
#     for tweet in public_tweets:
#         data = data +tweet.text
#     return HttpResponse(data)




def index(request):
    data = getStream()
    return HttpResponse(data)