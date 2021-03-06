"""grandExchange_web URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/user/', views.createUser, name='createUser'),
    path('create/item/', views.createListing, name='createListing'),
    path('', views.index, name='home'),
    path('detail/<int:num>/', views.detail, name='detail'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.updateProfile, name='updateProfile'),
    path('items/', views.showItems, name='showItems'),
    path('items/results/' , views.showResults, name='showResults'),
    path('items/results/popular/' , views.showResultsPopular, name='showResultsPopular')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)