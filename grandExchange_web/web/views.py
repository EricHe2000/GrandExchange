from django.shortcuts import render, redirect
import urllib.request
import urllib.parse
import json
import logging
from .forms import UserForm, LoginForm, ListingForm, UpdateProfileForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from urllib.error import HTTPError
from django.urls import reverse

def index(request):
    resp = {}
    login = isLoggedIn(request)
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
    return render(request, 'landing.html',context = {'cheap':sorted(dictCheap, key = lambda i: float(i['price'])),'hot':sorted(dictHot, key = lambda i: i['numberBought'],reverse=True),'login':login} )

def isLoggedIn(request):
    login = False
    auth = request.COOKIES.get('auth')
    if auth:
        data = {'authenticator': auth}
        authenticator = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request('http://exp:8000/api/v1/auth/check', authenticator)
        try:
            handler = urllib.request.urlopen(req).read().decode('utf-8')
            results = json.loads(handler)
            login = results["ok"]
        except KeyError as e:
            content = e
    return login

def detail(request,num=1):
    login = isLoggedIn(request)
    item_id = num
    user_id = request.COOKIES.get('user_id')
    
    data = {'user_id' : user_id, 'item_id' : item_id}
    data2 = urllib.parse.urlencode(data).encode('utf-8')

    print(data2)

    req = urllib.request.Request('http://exp:8000/api/v1/getItem/'+str(num)+'/', data=data2)

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    print(resp)
    return render(request, 'item.html',context = {'dict':resp,'login':login})

def createUser(request):
    login = isLoggedIn(request)
    if not login: 
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                data = urllib.parse.urlencode(form.cleaned_data).encode('utf-8')
                req = urllib.request.Request('http://exp:8000/api/v1/post/user', data)
                #resp_json = urllib.request.urlopen(req)
                try:
                    handler = urllib.request.urlopen(req).read().decode('utf-8')
                    results = json.loads(handler)
                    if not results["ok"]: #false means user already exists
                        return render(request, 'createUser.html', {'createUserFailed': True ,'userExists': results["ok"],'form': form})
                except HTTPError as e:
                    content = e.read()
                    return redirect("login")
                return redirect("login")
            else:
                return render(request, 'createUser.html', {'createUserFailed': True ,'userExists': False,'form': form})

        else:
            form = UserForm()

        return render(request, 'createUser.html', {'userExists': True,'form': form})
    else:
        return redirect("home")

def showItems(request):
    resp = {}
    login = isLoggedIn(request)
    if login:
        req = urllib.request.Request('http://exp:8000/api/v1/item/getAllItems')
        try:
            handler = urllib.request.urlopen(req).read().decode('utf-8')
            results = json.loads(handler)
            print(results)
            print(type(results))
        except HTTPError as e:
            content = e.read()
        return render(request, 'itemIndex.html',{'dict':results,'login':login})
    else:
        return redirect("login")

def showResults(request):
    resp = {}
    login = isLoggedIn(request)
    if login:
        if request.method == 'GET':

            data = {'query': request.GET['q']}
            data2 = urllib.parse.urlencode(data).encode('utf-8')
            req = urllib.request.Request('http://exp:8000/api/v1/item/getRequestedItems', data=data2)

            try:
                handler = urllib.request.urlopen(req).read().decode('utf-8')
                results = json.loads(handler)
                results = results['items']
            except HTTPError as e:
                return HttpResponse('Elastic Search container still loading... please reload in a few moments.')

            #return JsonResponse(results)
            return render(request, 'itemResults.html', {'dict': results, 'login': login})
        else:
            #redirect to all items
            return redirect("showItems")
    else:
        #redirect user to login
        return redirect("login")

def showResultsPopular(request):
    resp = {}
    login = isLoggedIn(request)
    if login:
        if request.method == 'GET':

            data = {'query': request.GET['q2']}
            data2 = urllib.parse.urlencode(data).encode('utf-8')
            req = urllib.request.Request('http://exp:8000/api/v1/item/getRequestedPopular', data=data2)

            try:
                handler = urllib.request.urlopen(req).read().decode('utf-8')
                results = json.loads(handler)
                results = results['items']
            except HTTPError as e:
                return HttpResponse('Elastic Search container still loading... please reload in a few moments.')

            return render(request, 'itemResults.html', {'dict': results, 'login': login})
        else:
            #redirect to all items
            return redirect("showItems")
    else:
        #redirect user to login
        return redirect("login")


def createListing(request):
    login = isLoggedIn(request)
    if login: # if actually valid
        if request.method == 'POST':
            form = ListingForm(request.POST)
            if form.is_valid():
                data = urllib.parse.urlencode(form.cleaned_data).encode('utf-8')
                
                req = urllib.request.Request('http://exp:8000/api/v1/post/item', data)
                try:
                    handler = urllib.request.urlopen(req).read().decode('utf-8')
                    results = json.loads(handler)
                    
                    return redirect("/detail/"+str(results[0]["id"])+"/")
                except HTTPError as e:
                    content = e.read()
                    return HttpResponse(content)
            #return HttpResponse("Thank you," + handler + 'your account has successfully been created. Return to Home to login and start creating listings!')
        else:
            form = ListingForm()
    else:
        return redirect("login")

    return render(request, 'createListing.html', {'form': form,'login':login})


"""
exp_srvc_errors.py: where I put some HTTP error status codes that the experience
service can return.
"""
def logout(request):
    auth = request.COOKIES.get('auth')
    if auth:
        data = {'authenticator': auth}
        authenticator = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request('http://exp:8000/api/v1/auth/logout', authenticator)
        try:
            handler = urllib.request.urlopen(req).read().decode('utf-8')
            results = json.loads(handler)
            login = results["ok"]
        except KeyError as e:
            content = e
    if login:
        logout(request)
        response = HttpResponseRedirect('/')
        response.delete_cookie('auth')
        response.delete_cookie('user_id')
        response.delete_cookie('userid')
        return response
    else:
        return HttpResponse("logout failed")

def login(request):
    login = isLoggedIn(request)
    # If we received a GET request instead of a POST request
    if not login: 
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
            resp = json.loads(handler)
        # Check if the experience layer said they gave us incorrect information
            if not resp or not resp['ok']:
        # Couldn't log them in, send them back to login page with error
                #return HttpResponseRedirect(reverse('login')) #add error message
                form = LoginForm()
                return render(request, 'loginUser.html',context = {'failedLogin':True,'form': form})
            authenticator = resp['data']['authenticator']
            user_id = resp['data']['user_id']
            date = resp['data']['date_created']


            response = HttpResponseRedirect(next)
            response.set_cookie("auth", authenticator)
            response.set_cookie('user_id', user_id)

            return response
        except HTTPError as e:
            content = e.read()

        return content
    else: 
        return redirect("home")
    """ If we made it here, we can log them in. """
    # Set their login cookie and redirect to back to wherever they came from

def profile(request):
    login = isLoggedIn(request)
    if login:
        num = request.COOKIES.get('user_id')
        #d = dict(num=num)
        #f = urllib.parse.urlencode(d).encode('utf-8')

        req = urllib.request.Request('http://exp:8000/api/v1/getUser/'+str(num))
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        return render(request, 'viewUser.html', context={'dict': resp, 'login':login})
        #return HttpResponse()
    else:
        return redirect('login')



def updateProfile(request):
    login = isLoggedIn(request)
    if login:  # if actually valid
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST)

            if form.is_valid():
                data = urllib.parse.urlencode(form.cleaned_data).encode('utf-8')
                num = request.COOKIES.get('user_id')

                req = urllib.request.Request('http://exp:8000/api/v1/user/' + str(num) + '/update', data)
                try:
                    handler = urllib.request.urlopen(req).read().decode('utf-8')
                    results = json.loads(handler)

                    return redirect("/profile/")
                except HTTPError as e:
                    content = e.read()
                    return HttpResponse(content)
                # return HttpResponse("Thank you," + handler + 'your account has successfully been created. Return to Home to login and start creating listings!')
        else:
            form = UpdateProfileForm()
    else:
        return redirect("login")

    return render(request, 'updateProfile.html', {'form': form})


