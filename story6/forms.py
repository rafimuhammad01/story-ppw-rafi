from django import forms

from .models import Person, Kegiatan

class PersonForm(forms.ModelForm):
    class Meta :
        model = Person
        fields = [
            'nama',
        ]

    


class KegiatanForm(forms.ModelForm):
    class Meta :
        model = Kegiatan
        fields = [
            'nama',
        ]