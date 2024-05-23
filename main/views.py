from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from main.models import User
from main.forms import RegisterForm
from main.forms import LoginForm
from django.contrib.auth import logout


class Registration(CreateView):
    template_name = "main/registration.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy("home")


class Login(LoginView):
    template_name = "main/login.html"
    model = User
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy("profile")


@login_required
def profile_view(request):
    user = request.user
    return render(request, 'main/profile.html', {'user': user})


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('home'))
