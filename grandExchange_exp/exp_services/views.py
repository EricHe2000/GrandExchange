from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
import urllib.request
import urllib.parse
import json
from django.http import JsonResponse, HttpResponse


def getItem(request,num=1):
    req = urllib.request.Request('http://models:8000/api/v1/item/'+str(num))
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    results = json.loads(resp_json)

    #dict = {"sold":results[0], 'title': 'tru', 'description' : 'yeye', 'price' : 6.5, 'id':4}

    return JsonResponse(results)

def getHottestCheapestList(request):
    req = urllib.request.Request('http://models:8000/api/v1/item/hottest')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    results = json.loads(resp_json)

    req1 = urllib.request.Request('http://models:8000/api/v1/item/cheapest')
    resp_json2 = urllib.request.urlopen(req1).read().decode('utf-8')
    results2 = json.loads(resp_json2)

    #dict = {"sold":results[0], 'title': 'tru', 'description' : 'yeye', 'price' : 6.5, 'id':4}
    if len(results) > 2:
        dict = {"Hottest1": results[0],"Hottest2": results[1] ,"Hottest3": results[2],"Hottest4": results[3] ,"Cheapest1": results2[0],"Cheapest2": results2[1],"Cheapest3": results2[2],"Cheapest4": results2[3]}
    else:
        dict = {}

    print(dict)
    return JsonResponse(dict)


#change this csrf exempt thing when we get tokens to work
@csrf_exempt
def postUser(request):
    name = request.POST.get('name', None)
    email = request.POST.get('email', None)
    age = request.POST.get('age', None)
    gender = request.POST.get('gender', None)
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    data_setup = {'name': name, 'email': email, 'age': age, 'gender': gender, 'username': username, 'password': password}
    data = urllib.parse.urlencode(data_setup).encode('utf-8')
    req = urllib.request.Request('http://models:8000/api/v1/user/create', data)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    results = json.loads(resp_json)
    return JsonResponse(results)

#change this csrf exempt thing when we get tokens to work
@csrf_exempt
def login(request):

    #add stuff here
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    data_setup = {'username': username, 'password': password}
    data = urllib.parse.urlencode(data_setup).encode('utf-8')
    req = urllib.request.Request('http://models:8000/api/v1/user/login', data)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    results = json.loads(resp_json)
    return JsonResponse(results)
