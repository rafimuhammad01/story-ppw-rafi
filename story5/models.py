from django.db import models

# Create your models here.
class MataKuliah(models.Model) :
    nama_matkul = models.CharField(max_length = 50)
    semester = models.CharField(max_length = 50)
    deskripsi = models.TextField(max_length = 500)
    sks = models.CharField(max_length = 50)

    def __str__(self) :
        return self.nama_matkul