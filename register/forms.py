from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

class Register(UserCreationForm):
    meh = 'meh'
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
