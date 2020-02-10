from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import User, Item
from django.core import serializers
from .forms import UserForm, ItemForm
from django.views.decorators.csrf import csrf_exempt

def homeView(request):
	return render(request, 'home.html')

@csrf_exempt
def createUser(request):
	if request.method == 'POST':
		form= UserForm(request.POST)
		if form.is_valid():
			form.save()
		users = User.objects.all().filter(pk=User.objects.all().count()).values()
		users_list = list(users)
		return JsonResponse(users_list, safe=False)
	else:
		return JsonResponse({'Error': 'No Post request, try again.'})

@csrf_exempt
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
	users = User.objects.all().filter(pk=userid).values()
	users_list = list(users)
	return JsonResponse(users_list, safe=False)

def getItem(request, itemid):
	items = Item.objects.all().filter(pk=itemid).values()
	items_list = list(items)
	return JsonResponse(items_list, safe=False)


def updateUser(request):
	return render(request,'test.html')


def updateItem(request):
	return render(request,'test.html')


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