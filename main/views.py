from django.shortcuts import render
from rest_framework import viewsets, generics
from main.serializers import UserSerializer, BuildingSerializer, OfficeSerializer, ProfileSerializer, Work_requestSerializer  
from main import models, serializers
from django.contrib.auth.models import User

class UserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BuildingAPIView(generics.CreateAPIView):
    queryset = models.Building.objects.all()
    serializer_class = BuildingSerializer    

class OfficeAPIView(generics.CreateAPIView):
    queryset = models.Office.objects.all()
    serializer_class = OfficeSerializer    

class ProfileAPIView(generics.CreateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer    

class Work_requestAPIView(generics.CreateAPIView): #viewsets.ModelViewSet
    queryset = models.Work_request.objects.all()
    serializer_class = Work_requestSerializer    

def home(response):
    return render(response, "main/home.html", {"name": "ursu"})