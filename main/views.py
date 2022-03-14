from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets          # add this
from main.urls import UserSerializer      # add this
from .models import Profile    

class ProfileView(viewsets.ModelViewSet):       # add this
    serializer_class = UserSerializer          # add this
    queryset = Profile.objects.all()

def home(response):
    return render(response, "main/home.html", {"name": "ursu"})