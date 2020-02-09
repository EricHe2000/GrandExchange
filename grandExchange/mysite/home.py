from django.shortcuts import render
from django.http import JsonResponse
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

def getItem(request):
	return render(request,'test.html')


def updateUser(request):
	return render(request,'test.html')


def updateItem(request):
	return render(request,'test.html')


def deleteUser(request):
	return render(request,'test.html')


def deleteItem(request):
	return render(request,'test.html')