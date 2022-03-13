from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(response):
    return render(response, "main/home.html", {"name": "ursu"})