from django.shortcuts import render, redirect
from .models import Person, Kegiatan
from .forms import KegiatanForm, PersonForm

# Create your views here.
def index(request) :
    formPerson = PersonForm()
    kegiatan = Kegiatan.objects.all()
    persons = Person.objects.all()
    id = 0

    if request.method == "POST" :
        if request.POST.get("addPerson") :
            id = request.POST.get("addPerson")
        if request.POST.get("addPersonToDatabase") :
            id = request.POST.get("addPersonToDatabase")
            formPerson = PersonForm(request.POST)
            if formPerson.is_valid() :
                person = formPerson.save()
                Kegiatan.objects.get(id=id).peserta.add(person)
                return redirect('story6:index')
        if request.POST.get("addKegiatan") : 
            return redirect('story6:add')
    context = {
        "kegiatan" : kegiatan,
        "persons" : persons,
        "pk" : int(id),
        "formPerson" : formPerson,
    }
    return render(request, "story6/index.html", context)

def add(request) :
    formKegiatan = KegiatanForm()

    if request.method == "POST" :
        formKegiatan = KegiatanForm(request.POST)
        if formKegiatan.is_valid() :
            formKegiatan.save()
            return redirect('story6:index')

    context = {
        "formKegiatan" : formKegiatan
    }

    return render(request, "story6/add.html", context)