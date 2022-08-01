from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.forms import RegisterForm

class RegisterUser(CreateView):
        model = User
        template_name = "accounts/register.html"
        form_class = RegisterForm
        success_url = reverse_lazy('village:home')
