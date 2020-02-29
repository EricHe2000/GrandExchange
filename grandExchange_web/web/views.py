from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import json
from django.http import HttpResponse
import urllib.request
import urllib.parse
# Create your views here.
def index(request):
    context_dict = {'newestpk':1}
    req = urllib.request.Request('http://exp:8002/api/v1/item/getLowestPricedItemPK')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    context_dict['newestpk'] = resp['result']['pk']
    return render(request, "index.html", context_dict)
