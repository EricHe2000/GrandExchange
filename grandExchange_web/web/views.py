from django.shortcuts import render
import urllib.request
import urllib.parse
import json
import logging


def index(request):
    req = urllib.request.Request('http://exp:8000/api/v1/item/hottestCheapestList')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    d = json.loads(resp_json)
    dictCheap = [d["Cheapest1"], d["Cheapest2"],d["Cheapest3"]]
    dictHot = [d["Hottest1"], d["Hottest2"],d["Hottest3"]]
    #resp_list = list(resp.values())
    return render(request, 'test.html',context = {'cheap':dictCheap,'hot':dictHot} )

def detail(request,num=1):

    req = urllib.request.Request('http://exp:8000/api/v1/getItem/'+str(num))

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return render(request, 'item.html',context = {'dict':resp})




