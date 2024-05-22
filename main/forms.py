from django.contrib.auth.forms import UserCreationForm
from django import forms

from main.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Введите имя пользователя",
                                                             "class": "form-control py-4",
                                                             "aria-describedby": "usernameHelp"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Введите email",
                                                          "class": "form-control py-4",
                                                          "aria-describedby": "emailHelp"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль",
                                                                  "class": "form-control py-4"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Повторите пароль",
                                                                  "class": "form-control py-4"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
