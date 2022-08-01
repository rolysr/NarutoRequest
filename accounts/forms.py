from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

        class Meta:
                model = User
                fields = [
                                'username',
                                'first_name',
                                'last_name',
                                'email',
                ]
                labels = {
                                'username': 'Username',
                                'first_name': 'Name',
                                'last_name': 'Last Name',
                                'email': 'E-Mail',
                }
