from django.shortcuts import render

# Create your views here.
import urllib.request
import urllib.parse
import json

def getItem(request):
    print("hellelooo")
    #req = urllib.request.Request('http://models:8001/api/v1/item/2/')
    #return req
