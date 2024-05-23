from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.Login.as_view(), name='login'),
]
