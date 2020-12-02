from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request) :
    return render(request, 'story8/index.html')

def data(request) :
    return HttpResponse("testing")