from django.shortcuts import render, redirect
from .models import Person, Kegiatan
from .forms import KegiatanForm, PersonForm

# Create your views here.
def index(request) :
    formPerson = PersonForm()
    formKegiatan = KegiatanForm()
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
    
    context = {
        "kegiatan" : kegiatan,
        "persons" : persons,
        "pk" : int(id),
        "formKegiatan" : formKegiatan,
        "formPerson" : formPerson,
    }
    return render(request, "story6/index.html", context)