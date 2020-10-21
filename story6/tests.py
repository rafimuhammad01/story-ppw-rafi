from django.test import TestCase, Client
from .views import index
from .models import Person, Kegiatan

# Create your tests here.



class MainTestCase(TestCase):
    def test_url(self) :
        response = Client().get("/story6/")
        self.assertEqual(response.status_code,200)

    def test_template_used(self) :
        response = Client().get("/story6/")
        self.assertTemplateUsed(response,"story6/index.html")

    def test_template_tanpa_kegiatan(self) :
        response = Client().get('/story6/')
        html_response = response.content.decode('utf8')
        self.assertIn("Tidak Ada Kegiatan", html_response)
        self.assertIn("Add Activities", html_response)

    def test_model_person(self) :
        Person.objects.create(nama="Coba Nama")
        count = Person.objects.count()
        self.assertEqual(count, 1)

    def test_model_kegiatan(self) :
        create_person = Person.objects.create(nama="Coba Nama")
        person = Person.objects.get(id=create_person.id)
        kegiatan = Kegiatan.objects.create(nama='Kegiatan 1')
        kegiatan.peserta.add(person)
        count = Kegiatan.objects.count()
        self.assertEqual(count,1)

    def test_button_add_kegiatan(self) :
        pass

    def test_button_add_person(self) :
        pass

    def test_template_dengan_kegiatan_tanpa_person(self) :
        kegiatan = Kegiatan.objects.create(nama='Kegiatan 1')
        response = Client().get('/story6/')
        html_response = response.content.decode('utf8')
        self.assertIn("Tidak Ada Peserta", html_response)
        self.assertIn("Add", html_response)
        self.assertIn("Add Activities", html_response)


    def test_template_dengan_kegiatan_dan_person(self) :
        create_person = Person.objects.create(nama="Coba Nama")
        person = Person.objects.get(id=create_person.id)
        kegiatan = Kegiatan.objects.create(nama='Kegiatan 1')
        kegiatan.peserta.add(person)
        response = Client().get('/story6/')
        html_response = response.content.decode('utf8')
        self.assertIn("Coba Nama", html_response)
        self.assertIn("Add", html_response)
        self.assertIn("Add Activities", html_response)

   
