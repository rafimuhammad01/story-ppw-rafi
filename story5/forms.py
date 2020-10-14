from django import forms

from .models import MataKuliah

class MataKuliahForm(forms.ModelForm):


    class Meta :
        model = MataKuliah
        fields = [
            'nama_matkul',
            'semester',
            'deskripsi'
        ]