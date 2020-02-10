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
		form.save()
		return JsonResponse({'Message':'Post request'})
	else:
		return JsonResponse({'Message':'No Post request'})

@csrf_exempt
def createItem(request):
	if request.method == 'POST':
		form= ItemForm(request.POST)
		if form.is_valid():
			form.save()
		return JsonResponse({'Message':'Post request'})
	else:
		return JsonResponse({'Message':'No Post request'})

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