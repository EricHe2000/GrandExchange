from django.shortcuts import render

# Create your views here.
import urllib.request
import urllib.parse
import json
from django.http import JsonResponse, HttpResponse

def getItem(request):

    req = urllib.request.Request('http://models:8000/api/v1/item/4/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    results = json.loads(resp_json)

    #dict = {"sold":results[0], 'title': 'tru', 'description' : 'yeye', 'price' : 6.5, 'id':4}

    return JsonResponse(results)

def getHottestList(request):
    req = urllib.request.Request('http://models:8000/api/v1/item/hottest')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    results = json.loads(resp_json)

    #dict = {"sold":results[0], 'title': 'tru', 'description' : 'yeye', 'price' : 6.5, 'id':4}
    if len(results) > 2:
        dict = {"first": results[0], "second": results[1],"third":results[2] }
    else:
        dict = {}
    return JsonResponse(dict)