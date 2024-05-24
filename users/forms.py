from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from users.models import User


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


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Введите имя пользователя",
                                                             "class": "form-control py-4",
                                                             "aria-describedby": "usernameHelp"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль",
                                                                 "class": "form-control py-4"}))

    class Meta:
        model = User
        fields = ('username', 'password')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'profile_picture')


class CustomUserDeleteForm(forms.Form):
    confirm = forms.BooleanField(label="Are you sure you want to delete your account?")

