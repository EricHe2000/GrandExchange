import datetime
from django.conf import settings
import os
import hmac
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import User, Item, Authenticator
from django.core import serializers
from .forms import UserForm, ItemForm, LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
def createUser(request):
	response = {}
	if request.method == 'POST':
		form = UserForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			if User.objects.filter(username=username):
				response['ok'] = False
			else:
				response['ok'] = True			
				name = form.cleaned_data['name']
				email = form.cleaned_data['email']
				age = form.cleaned_data['age']
				gender = form.cleaned_data['gender']
				password1 = form.cleaned_data['password']
				password = make_password(password1)
				user = User(name=name,email=email,age=age,gender=gender, username=username,password=password)
				user.save()
			#return_val = User.objects.all().filter(pk=User.objects.all().count()+2).values()
			return JsonResponse(response)
	else:
		return JsonResponse({'Error': 'No Post request, try again.'}, safe=False)

def loginUser(request):
	response = {}
	authData = {}
	if request.method == 'POST':
		form = LoginForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password'] 
			if User.objects.filter(username=username):
				user = User.objects.get(username=username)
				print(user.password)
				if check_password(password, user.password):
					print("checked password")
					authObj = Authenticator()
					authObj.user_id = user.pk
					authObj.is_valid = True
					authObj.date_created = datetime.date.today()
					if Authenticator.objects.filter(user_id=user.pk):
						authCheck = Authenticator.objects.get(user_id=user.pk)
						authObj.authenticator = authCheck.authenticator
						print("auth already exists")
					else:
						authenticator = ""
						authenticator = hmac.new(
								key = settings.SECRET_KEY.encode('utf-8'),
								msg = os.urandom(32),
								digestmod = 'sha256',
							).hexdigest()
						authObj.authenticator = authenticator
						print(authenticator)
					authObj.save()
					authData['user_id'] = authObj.user_id
					authData['is_valid'] = authObj.is_valid
					authData['date_created'] = authObj.date_created
					authData['authenticator'] = authObj.authenticator
					response['ok'] = True
					response['data'] = authData
				else:
					response['ok'] = False
			else:
				response['ok'] = False
		return JsonResponse(response)
	else:
		return JsonResponse({'Error': 'No Post request, try again.'}, safe=False)

def checkAuth(request):
	response = {}
	user_auth = request.POST.get('authenticator', None)
	if user_auth is None:
		 response['ok'] = False
	try:
		authObj = Authenticator.objects.get(authenticator = user_auth)
	except Authenticator.DoesNotExist:
		authObj = None
	if authObj is not None:
		try:
			user = User.objects.get(pk = authObj.user_id)
		except User.DoesNotExist:
			user = None
		if user is not None:
			response['userid'] = authObj.user_id
			response['ok'] = True
		else:
			response['ok'] = False
	return JsonResponse(response)

def logout(request):
	response = {}
	user_auth = request.POST.get('authenticator', None)
	if user_auth is None:
		 response['ok'] = False
	try:
		authObj = Authenticator.objects.get(authenticator = user_auth)
	except Authenticator.DoesNotExist:
		authObj = None
	if authObj is not None:
		authObj.delete()
		response['ok'] = True
	else:
		response['ok'] = False
	return JsonResponse(response)

def createItem(request):
	if request.method == 'POST':
		form= ItemForm(request.POST)
		if form.is_valid():
			form.save()
		items = Item.objects.all().filter(pk=Item.objects.all().count()).values()
		items_list = list(items)
		return JsonResponse(items_list, safe=False)
	else:
		return JsonResponse({'Error': 'No Post request, try again.'})

def getUser(request, userid):
	user = User.objects.all().filter(pk=userid)
	if user.exists():
		user_list = list(user.values())
		return JsonResponse(user_list, safe=False)	
	else:
		return JsonResponse({'Error': 'User does not exist'}) 

def getItem(request, itemid):
	item = Item.objects.all().filter(pk=itemid)
	if item.exists():
		item_list = list(item.values())
		return JsonResponse(item_list[0], safe=False)
	else:
		return JsonResponse({'Error': 'Item does not exist'})

def getHottestItem(request):
	items = Item.objects.all().order_by('numberBought').reverse()
	if items.exists():
		item_list = list(items.values())
		return JsonResponse(item_list, safe=False)
	else:
		return JsonResponse({'Error': 'Item does not exist'})


def getCheapestItem(request):
	items = Item.objects.all().order_by('price')
	if items.exists():
		item_list = list(items.values())
		return JsonResponse(item_list, safe=False)
	else:
		return JsonResponse({'Error': 'Item does not exist'})

@csrf_exempt
def updateUser(request, userid):

	if request.method == 'POST':
		user = User.objects.all().filter(pk=userid)
		if request.POST.get('name') != None:
			user.update(name=request.POST.get('name'))
		if request.POST.get('email') != None:
			user.update(email=request.POST.get('email'))
		if request.POST.get('age') != None:
			user.update(age=request.POST.get('age'))
		if request.POST.get('gender') != None:
			user.update(gender=request.POST.get('gender'))

		users_list = list(user.values())
		return JsonResponse(users_list, safe=False)

	else:
		return JsonResponse({'Error': 'Couldn\'t update'})

@csrf_exempt
def updateItem(request, itemid):
	if request.method == 'POST':
		item = Item.objects.all().filter(pk=itemid)

		if request.POST.get('sold') != None:
			item.update(sold=request.POST.get('sold'))
		if request.POST.get('title') != None:
			item.update(title=request.POST.get('title'))
		if request.POST.get('description') != None:
			item.update(description=request.POST.get('description'))
		if request.POST.get('price') != None:
			item.update(price=request.POST.get('price'))

		items_list = list(item.values())

		return JsonResponse(items_list, safe=False)

	else:
		return JsonResponse({'Error': 'Couldn\'t update'})


def deleteUser(request, userid):
	user = User.objects.all().filter(pk=userid)
	if user.exists():
		user.delete()
		return JsonResponse({'Success': 'Your user has been deleted.'})
	else:
		return JsonResponse({'Error': 'User either doesn\'t exist or has already been deleted.'})


def deleteItem(request, itemid):
	item = Item.objects.all().filter(pk=itemid)
	if item != None:
		item.delete()
		return JsonResponse({'Success': 'Your item has been deleted.'})
	else:
		return JsonResponse({'Error': 'Item either doesn\'t exist or has already been deleted.'})