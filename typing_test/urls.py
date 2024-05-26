from django.urls import path
from .views import typing_test, add_text

urlpatterns = [
    path('test/', typing_test, name='typing_test'),
    path('text/add/', add_text, name='add_text'),
]
