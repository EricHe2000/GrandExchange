from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import User, Item
from django.core import serializers
from .forms import UserForm, ItemForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def createUser(request):
	if request.method == 'POST':
		form = UserForm(data=request.POST)
		if form.is_valid():

			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			age = form.cleaned_data['age']
			gender = form.cleaned_data['gender']

			user = User(name,email,age,gender)
			user.save()

			return JsonResponse({'id': 'hello'})
		else:
			return JsonResponse({'Error': 'No Post request, try again.'})


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