from django import forms
from .models import User, Item

class ItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields= ["sold", "user", "title","description","price"]

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields= ["name", "email", "age", "gender"]
