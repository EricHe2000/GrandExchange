from django.shortcuts import render
import urllib.request
import urllib.parse
import json
import logging
from .forms import UserForm, LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from urllib.error import HTTPError
from django.urls import reverse

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
            #resp_json = urllib.request.urlopen(req)
            try:
                handler = urllib.request.urlopen(req).read().decode('utf-8')
            except HTTPError as e:
                content = e.read()
                return HttpResponse(content)
            #resp = json.loads(handler)
            return HttpResponse(handler)
            #return HttpResponse('Thank you , your account has successfully been created. Return to Home to login and start creating listings!')
        else:

            return HttpResponse("please fix issues!")

    else:
        form = UserForm()

    return render(request, 'createUser.html', {'form': form})

"""
exp_srvc_errors.py: where I put some HTTP error status codes that the experience
service can return.
"""


def login(request):
    # If we received a GET request instead of a POST request
    
    if request.method == 'GET':
        # display the login form page
        form = LoginForm()
        return render(request, 'loginUser.html', {'form': form})

    # Creates a new instance of our login_form and gives it our POST data
    f = LoginForm(request.POST)

    # Check if the form instance is invalid
    if not f.is_valid():
      # Form was bad -- send them back to login page and show them an error
      form = LoginForm()
      return render(request, 'loginUser.html', {'form': form})

    # Sanitize username and password fields
    #username = f.cleaned_data['username']
    #password = f.cleaned_data['password']
    data = urllib.parse.urlencode(f.cleaned_data).encode('utf-8')

    # Get next page
    next = reverse('home')

    # Send validated information to our experience layer
    req = urllib.request.Request('http://exp:8000/api/v1/login/user', data = data, method= 'POST')
    try:
        handler = urllib.request.urlopen(req).read().decode('utf-8')
    except HTTPError as e:
        content = e.read()
    resp = json.loads(handler)
    # Check if the experience layer said they gave us incorrect information
    if not resp or not resp['ok']:
      # Couldn't log them in, send them back to login page with error
      return HttpResponse("please fix issues!FIX LATER")

    """ If we made it here, we can log them in. """
    # Set their login cookie and redirect to back to wherever they came from
    authenticator = resp['resp']['authenticator']

    response = HttpResponseRedirect(next)
    response.set_cookie("auth", authenticator)

    return response



