from django.db import models

# Create your models here.

class Person(models.Model) :
    nama = models.CharField(max_length=50)

class Kegiatan(models.Model) :
    nama = models.CharField(max_length=50)
    peserta = models.ManyToManyField(Person, null=True, blank=True)
