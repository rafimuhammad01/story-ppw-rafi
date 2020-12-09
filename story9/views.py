from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def index(request) :
    return render(request, 'story9/index.html')

def user_login(request) :
    if request.user.is_authenticated:
        return redirect('story9:index')
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('story9:index')
        else :
            context = {'failed': 'please check ur username or password'}
            return render(request, 'story9/login.html', context)
    return render(request, 'story9/login.html')

def user_signUp(request) :
    form = UserCreationForm()
    if request.user.is_authenticated:
        return redirect('story9:index')

    if request.method == "POST" :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
            login(request, new_user)
            return redirect('story9:login')

    context = {'form' : form}
    return render(request, 'story9/signup.html', context)

def logout_user(request) :
    logout(request)
    return redirect('story9:index')