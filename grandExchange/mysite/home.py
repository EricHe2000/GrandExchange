from django.shortcuts import render

def homeView(request):
	return render(request, 'home.html')

def createUser(request):
	return render(request,'test.html')

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