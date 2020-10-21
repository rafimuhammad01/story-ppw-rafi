from django.db import models

# Create your models here.

class Person(models.Model) :
    nama = models.CharField(max_length=50)

    def __str__(self) :
        return self.nama

class Kegiatan(models.Model) :
    nama = models.CharField(max_length=50)
    peserta = models.ManyToManyField(Person, blank=True)

    def __str__(self) :
        return self.nama
