from django.shortcuts import render
from .models import Person, Kegiatan

# Create your views here.
def index(request) :
    kegiatan = Kegiatan.objects.all()
    persons = Person.objects.all()
    context = {
        "kegiatan" : kegiatan,
        "persons" : persons
    }
    return render(request, "story6/index.html", context)