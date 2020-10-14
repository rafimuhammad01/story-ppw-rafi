from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MataKuliah
from .forms import MataKuliahForm

# Create your views here.

def index(request) :
    mataKuliah = MataKuliah.objects.order_by("semester")
    

    if request.POST.get('add') :
        return redirect('story5:add')

    context = {
        "mataKuliah" : mataKuliah,
    }
    return render(request, 'story5/index.html', context)

def add(request) :
    form = MataKuliahForm()
    if request.method == "POST" :
        form = MataKuliahForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('story5:index')
    context = {
        "form" : form
    }
    return render(request, 'story5/add.html', context)

def detail(request, id) :
    mataKuliah = MataKuliah.objects.get(id=id)
    if request.POST.get('update') :
        return redirect('story5:update', request.POST.get('update'))
    if request.POST.get('delete') :
        MataKuliah.objects.get(id=request.POST.get('delete')).delete()
        return redirect('story5:index')
    context = {
        'mataKuliah' : mataKuliah
    }
    return render(request, 'story5/detail.html', context)

def update(request, id) :
    form = MataKuliahForm(instance=MataKuliah.objects.get(id=id))
    if request.method == "POST" :
        form = MataKuliahForm(request.POST, instance=MataKuliah.objects.get(id=id))
        if form.is_valid() :
            form.save()
            return redirect('story5:index')
    context = {
        "form" : form,
        "update" : True
    }
    return render(request, 'story5/add.html', context)