from django.shortcuts import render

# Create your views here.

def index(request) :
    print(request)
    return render(request, 'story2/index.html')


def about(request) :
	return render(request, 'story2/about.html')
