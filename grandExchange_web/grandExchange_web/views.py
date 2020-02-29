from django.shortcuts import render
from django.http import JsonResponse
import json
from django.http import HttpResponse
import urllib.request
import urllib.parse

def index(request):
	return render(request, 'home.html')

def getLowestPricedItemPK(request):
    response = {}
    response_data = {}
    req = urllib.request.Request('http://models-api:8000/api/v1/item/getLowestPricedItem')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    results = json.loads(resp_json)

    newest_pk = results["result"]["pk"]
    response_data["pk"] = newest_pk

    response['result'] = response_data
    return JsonResponse(response)
