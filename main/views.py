from django.shortcuts import render
from django.views.generic import CreateView
from main.models import User
from main.forms import RegisterForm


class Registration(CreateView):
    template_name = "main/registration.html"
    model = User
    form_class = RegisterForm

    # def post(self, request, *args, **kwargs):
    #


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')
