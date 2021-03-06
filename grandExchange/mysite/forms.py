from django import forms
from .models import User, Item

class ItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields= ["sold", "title","description","price","numberBought"]

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields= ["name", "email", "age", "gender","username", "password"]

class LoginForm(forms.ModelForm):
    class Meta:
        model= User
        fields= ["username", "password"]