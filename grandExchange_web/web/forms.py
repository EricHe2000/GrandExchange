from django.forms import ModelForm
from django import forms

class CreateUserForm(forms.Form):
    uniquename = forms.CharField(max_length=200, help_text="Username: ")
    password = forms.CharField(widget=forms.PasswordInput(), max_length=200, help_text="Password: ")
    first_name = forms.CharField(max_length=200, help_text="First Name: ")
    last_name = forms.CharField(max_length=200, help_text="Last Name: ")
    age = forms.DecimalField(max_digit=3, help_text="Age: ")
    email = forms.CharField(max_length=200, help_text="Email Address: ")