from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html", {"name": "ursu"})

def create(response):
    return render(response, "main/create.html", {"name": "kalu"})
