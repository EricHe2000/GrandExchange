from django.shortcuts import render
import urllib.request
import urllib.parse
import json
import logging


def index(request):
    req = urllib.request.Request('http://exp:8000/api/v1/item/hottestCheapestList')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return render(request, 'test.html',{'dict':resp})

def detail(request):

    req = urllib.request.Request('http://exp:8000/api/v1/getItem')

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    #print(resp)
    return render(request, 'item.html',context=resp)




