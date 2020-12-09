from django.shortcuts import render

# Create your views here.


def index(request) :
    return render(request, 'story9/index.html')

def login(request) :
    return render(request, 'story9/login.html')