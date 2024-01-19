from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world") 

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def home(request):
    return render(request,"home.html")

def landing(request):
    return render(request,"landing.html")

def about(request):
    return render(request,"about.html")

def profile(request):
    return render(request,"profile.html")