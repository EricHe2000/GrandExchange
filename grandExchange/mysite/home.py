from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import User, Item
from django.core import serializers
from .forms import UserForm, ItemForm
from django.views.decorators.csrf import csrf_exempt

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

def getLowestPricedItem(request):
    response = {}
    response_data = {}

    try:
        #Gets lowest priced item
        item = Item.objects.filter().latest('price')
        response_data['pk'] = item.pk
        response_data['title'] = item.title
        response_data['description'] = item.description
        response_data['price'] = item.price
        response_data['sold'] = item.sold
    except:
        return JsonResponse({'Error': 'Lowest priced item not found'})

    response['result'] = response_data
    return JsonResponse(response)