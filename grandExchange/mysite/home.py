from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import User, Item
from django.core import serializers

def homeView(request):
	return render(request, 'home.html')

def createUser(request):
	return render(request, 'test.html')


def createItem(request):
	return render(request,'test.html')

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
	users = User.objects.all().filter(pk=userid).delete()
	return HttpResponse("Your user has been deleted")


def deleteItem(request, itemid):
	items = Item.objects.all().filter(pk=itemid).delete()
	return HttpResponse("Your item has been deleted")