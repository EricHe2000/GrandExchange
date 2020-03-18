from django import forms
from django.forms import PasswordInput

from django.core.validators import RegexValidator

passwordValidator = RegexValidator(
    regex='^[a-zA-Z0-9@$!%*#?&]*$',
    message='Password must only contain a-z, A-Z, 0-9, @$!%*#?&',
    code='invalid_password'
)

class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=50)
    age = forms.DecimalField(max_digits=3, decimal_places=0)
    gender = forms.CharField(max_length=100)
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, validators=[passwordValidator], widget=PasswordInput())
