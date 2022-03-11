from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import angajati

def home(response):
    return render(response, "main/home.html", {"name": "ursu"})