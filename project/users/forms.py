#  Forms that inherit from form(UserCreation)
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # required=True) = default

    class Meta:
        ## class Meta gives us a nested namespace for config, and keeps config in 1 place
        ## model that will be affected, User model
        ## fields that we have are in order
        model = User
        fields = ['username', 'email', 'password1', 'password2']