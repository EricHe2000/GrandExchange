from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from urllib.error import HTTPError
# Create your views here.
import urllib.request
import urllib.parse
import json
from django.http import JsonResponse, HttpResponse
import time
from kafka import KafkaProducer
from elasticsearch import Elasticsearch


def getItem(request,num=1):
    req = urllib.request.Request('http://models:8000/api/v1/item/'+str(num))
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    results = json.loads(resp_json)

    #dict = {"sold":results[0], 'title': 'tru', 'description' : 'yeye', 'price' : 6.5, 'id':4}

    return JsonResponse(results)




@csrf_exempt
def getUser(request, num=1):
    #num = request.GET['data']

    req = urllib.request.Request('http://models:8000/api/v1/user/' +str(num))
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    results = json.loads(resp_json)

    #dict = {"sold":results[0], 'title': 'tru', 'description' : 'yeye', 'price' : 6.5, 'id':4}

    return JsonResponse(results)

@csrf_exempt
def updateUser(request, num=1):
    name = request.POST.get('name', None)
    email = request.POST.get('email', None)
    gender = request.POST.get('gender', None)
    password = request.POST.get('password', None)
    #dealing with the weird case of having a non given age
    if request.POST.get('age', None) == 'None':
        age = 0
    else:
        age = request.POST.get('age', None)

    data_setup = {'name': name,'email': email, 'age': age, 'gender': gender,'password': password}
    data = urllib.parse.urlencode(data_setup).encode('utf-8')
    req = urllib.request.Request('http://models:8000/api/v1/user/'+str(num)+'/update', data)
    try:
        handler = urllib.request.urlopen(req).read().decode('utf-8')
    except HTTPError as e:
        content = e.read()
        return HttpResponse(content)
    results = json.loads(handler)
    return JsonResponse(results, safe=False)



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
    return JsonResponse(dict)

def getAllItems(request):
    req = urllib.request.Request('http://models:8000/api/v1/item/getAll')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    results = json.loads(resp_json)
    return JsonResponse(results,safe = False)

@csrf_exempt
def getRequestedItems(request):
    #we dont need to call models here.... we just see what elastic search has for us.
    query = request.POST['query']
    dict = {'0': query}
    es = Elasticsearch(['es'])

    results = es.search(index='listing_index', body={'query': {'query_string': {'query': query}}, 'size': 10})

    #results = results['hits']['hits']
    #return JsonResponse(dict)
    return JsonResponse(results,safe = False)


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
    try:
        handler = urllib.request.urlopen(req).read().decode('utf-8')
    except HTTPError as e:
        content = e.read()
        return HttpResponse(content)
    results = json.loads(handler)
    return JsonResponse(results, safe = False)

#change this csrf exempt thing when we get tokens to work
@csrf_exempt
def postItem(request):
    #checkAuth = urllib.request.Request('http://models:8000/api/v1/auth/check', data)
    sold = request.POST.get('sold', None)
    title = request.POST.get('title', None)
    description = request.POST.get('description', None)
    price = request.POST.get('price', None)
    numberBought = request.POST.get('numberBought', None)

    data_setup = {'sold': sold, 'title': title, 'description': description, 'price': price, 'numberBought': numberBought}
    data = urllib.parse.urlencode(data_setup).encode('utf-8')
    req = urllib.request.Request('http://models:8000/api/v1/item/create', data)




    try:
        handler = urllib.request.urlopen(req).read().decode('utf-8')
    except HTTPError as e:
        content = e.read()


    results = json.loads(handler)



    # send data our kafka queue
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    #get ID to pass into queue as well. possibly use for elastic search? (besides other fields)
    data_setup['id'] = results[0]['id']
    producer.send('newItem', json.dumps(data_setup).encode('utf-8'))

    return JsonResponse(results, safe = False)


#change this csrf exempt thing when we get tokens to work
@csrf_exempt
def login(request):
    response = {}
    
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    data_setup = {'username': username, 'password': password}
    data = urllib.parse.urlencode(data_setup).encode('utf-8')
    req = urllib.request.Request('http://models:8000/api/v1/user/login', data)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    results = json.loads(resp_json)
    return JsonResponse(results)

@csrf_exempt
def logout(request):
    auth = request.POST.get('authenticator', None)

    data_setup = {'authenticator': auth}
    data = urllib.parse.urlencode(data_setup).encode('utf-8')
    req = urllib.request.Request('http://models:8000/api/v1/auth/logout', data)
    
    try:
        handler = urllib.request.urlopen(req).read().decode('utf-8')
    except HTTPError as e:
        content = e.read()
        return HttpResponse(content)
    results = json.loads(handler)
    return JsonResponse(results, safe = False)

@csrf_exempt
def checkAuth(request):
    
    auth = request.POST.get('authenticator', None)

    data_setup = {'authenticator': auth}
    data = urllib.parse.urlencode(data_setup).encode('utf-8')
    req = urllib.request.Request('http://models:8000/api/v1/auth/check', data)
    
    try:
        handler = urllib.request.urlopen(req).read().decode('utf-8')
    except HTTPError as e:
        content = e.read()
        return HttpResponse(content)
    results = json.loads(handler)
    return JsonResponse(results, safe = False)