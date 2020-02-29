from django.shortcuts import render
import urllib.request
import urllib.parse
import json
import logging


def index(request):

    print('hellooo')

    logging.debug("Oh hai!")
    #req = urllib.request.Request('http://placeholder.com/v1/api/posts/1')

    #resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    #resp = json.loads(resp_json)

    return render(request, 'home.html')

def detail(request):
    logging.debug("Oh hai!")


    req = urllib.request.Request('http://exp:8002/v1/api/getItem/')

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    print(resp)

    return render(request, 'item.html', context=resp)




