from django.shortcuts import render
from django.http import JsonResponse

def homeView(request):
	return render(request, 'home.html')

def createUser(request):
	comments = [
		{'name' : 'Yang Tang', 'email': '@yang.com', 'age':'20','gender':'Male','interests': ["a"]},
	]
	return JsonResponse({'comments': comments})


def createItem(request):
	return render(request,'test.html')

def getUser(request):
	return render(request,'test.html')

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