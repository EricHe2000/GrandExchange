from django.shortcuts import render
import urllib.request
import urllib.parse
import json
import logging
from .forms import UserForm
from django.http import HttpResponse


def index(request):
    req = urllib.request.Request('http://exp:8000/api/v1/item/hottestCheapestList')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    d = json.loads(resp_json)
    dictCheap = []
    dictHot = []
    for name in d.keys():
        if "cheapest" in name.lower():
            dictCheap.append(d[name])

    for name in d.keys():
        if "hottest" in name.lower():
            dictHot.append(d[name])
                
    #resp_list = list(resp.values()) sorted(a_list, key=lambda price: float(price['dep_price']))
    return render(request, 'landing.html',context = {'cheap':sorted(dictCheap, key = lambda i: float(i['price'])),'hot':sorted(dictHot, key = lambda i: i['numberBought'],reverse=True)} )

def detail(request,num=1):

    req = urllib.request.Request('http://exp:8000/api/v1/getItem/'+str(num))

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return render(request, 'item.html',context = {'dict':resp})

def createUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            data = urllib.parse.urlencode(form.cleaned_data).encode('utf-8')

            req = urllib.request.Request('http://exp:8000/api/v1/post/user', data)
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            resp = json.loads(resp_json)

            return HttpResponse("User number " + str(resp['id']) + " has been successfully created.")
        else:

            return HttpResponse("please fix issues!")

    else:
        form = UserForm()

    return render(request, 'test.html', {'form': form})







