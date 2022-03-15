# urls.py
from django.urls import path, include
from django.contrib.auth.models import User
from main import views
urlpatterns = [
    path("", views.home, name = "home"),
]
