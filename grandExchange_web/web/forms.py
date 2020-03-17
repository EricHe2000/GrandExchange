from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=50)
    age = forms.DecimalField(max_digits=3, decimal_places=0)
    gender = forms.CharField(max_length=100)
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
