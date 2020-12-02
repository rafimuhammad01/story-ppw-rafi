from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import requests

# Create your views here.


def index(request) :
    return render(request, 'story8/index.html')

def data(request) :
    try :
        arugment = request.GET['q']
    except :
        arugment = ""
    url = 'https://www.googleapis.com/books/v1/volumes?q=' + arugment
    data = requests.get(url).json()

    return JsonResponse(data)