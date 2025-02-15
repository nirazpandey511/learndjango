# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),  # The empty string '' maps to the home page
]
