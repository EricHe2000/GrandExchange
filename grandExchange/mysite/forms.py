from django import forms
from .models import User, Item

class ItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields= ["sold", "title","description","price"]

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields= ["uniquename", "password", "first_name", "last_name","email","age"]
