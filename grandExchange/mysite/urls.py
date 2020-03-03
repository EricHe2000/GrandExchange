"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import home


# def homeView(request):
# 	return render(request, 'home.html')
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/user/create/', home.createUser, name='createUser'),
    path('api/v1/item/create/', home.createItem, name='createItem'),

    path('api/v1/user/<int:userid>/', home.getUser, name='getUser'),
    path('api/v1/item/<int:itemid>/', home.getItem, name='getItem'),

    path('api/v1/user/<int:userid>/update', home.updateUser, name='updateUser'),
    path('api/v1/item/<int:itemid>/update', home.updateItem, name='updateItem'),

    path('api/v1/user/<int:userid>/delete', home.deleteUser, name='deleteUser'),
    path('api/v1/item/<int:itemid>/delete', home.deleteItem, name='deleteItem'),

    path('api/v1/item/hottest', home.getHottestItem, name='getHottestItem'),
    path('api/v1/item/cheapest', home.getCheapestItem, name='getCheapestItem'),
]

