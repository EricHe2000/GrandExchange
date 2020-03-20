from django import forms
from django.forms import PasswordInput

from django.core.validators import RegexValidator

passwordValidator = RegexValidator(
    regex='^[a-zA-Z0-9@$!%*#?&]*$',
    message='Password must only contain a-z, A-Z, 0-9, @$!%*#?&',
    code='invalid_password'
)

GENDER_CHOICES =( 
    ("Male", "Male"), 
    ("Female", "Female"), 
    ("Genderqueer/Non-Binary", "Genderqueer/Non-Binary"), 
    ("Prefer not to disclose", "Prefer not to disclose"),
) 

class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=50)
    age = forms.DecimalField(max_digits=3, decimal_places=0)
    gender = forms.ChoiceField(choices = GENDER_CHOICES)
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

class ListingForm(forms.Form):
    sold = forms.BooleanField(required=False)
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=150)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    numberBought = forms.IntegerField()

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, validators=[passwordValidator], widget=PasswordInput())

class UpdateProfileForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=50, required=False)
    age = forms.DecimalField(max_digits=3, decimal_places=0, required=False)
    gender = forms.ChoiceField(choices = GENDER_CHOICES)

