from django import forms
from django.contrib.auth.models import AbstractUser


class LoginForm(AbstractUser):
    username = forms.CharField(widget=username)
    password = forms.PasswordInput()