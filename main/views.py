from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from main.models import User
from main.forms import RegisterForm
from main.forms import LoginForm


class Registration(CreateView):
    template_name = "main/registration.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy("home")


class Login(LoginView):
    template_name = "main/login.html"
    model = User
    form_class = LoginForm
    success_url = reverse_lazy("main/profile.html")


@login_required
def profile_view(request):
    return render(request, 'main/profile.html')


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')
