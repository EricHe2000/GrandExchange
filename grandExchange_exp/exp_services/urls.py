"""grandExchange_exp URL Configuration

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/getItem/<int:num>/', views.getItem),
    path('api/v1/getUser/<int:num>/', views.getUser),
    path('api/v1/item/hottestCheapestList', views.getHottestCheapestList),
    path('api/v1/post/user', views.postUser),
    path('api/v1/post/item', views.postItem),
    path('api/v1/login/user', views.login),
    path('api/v1/auth/check', views.checkAuth),
    path('api/v1/auth/logout', views.logout),
    path('api/v1/user/<int:num>/update', views.updateUser),
    path('api/v1/item/getAllItems', views.getAllItems)
    
]
