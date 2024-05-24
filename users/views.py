from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from users.forms import RegisterForm, LoginForm, CustomUserChangeForm
from users.models import User


class Registration(CreateView):
    template_name = "users/registration.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy("home")


class Login(LoginView):
    template_name = "users/login.html"
    model = User
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy("profile")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('home'))


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
        return render(request, 'users/update_profile.html', {'form': form})



