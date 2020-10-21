from django.test import TestCase, Client
from .views import index
from .models import Person, Kegiatan
from .forms import PersonForm, KegiatanForm

# Create your tests here.



class MainTestCase(TestCase):
    def test_url(self) :
        response = Client().get("/story6/")
        self.assertEqual(response.status_code,200)

        response = Client().get("/story6/add/")
        self.assertEqual(response.status_code,200)


    def test_template_used(self) :
        response = Client().get("/story6/")
        self.assertTemplateUsed(response,"story6/index.html")

        response = Client().get("/story6/add/")
        self.assertTemplateUsed(response,"story6/add.html")

    def test_template_tanpa_kegiatan(self) :
        response = Client().get('/story6/')
        html_response = response.content.decode('utf8')
        self.assertIn("Tidak Ada Kegiatan", html_response)
        self.assertIn("Add Activities", html_response)

    def test_model_person(self) :
        person1 = Person.objects.create(nama="Coba Nama")
        count = Person.objects.count()
        self.assertEqual(count, 1)

        self.assertEqual(str(person1), "Coba Nama")

    def test_model_kegiatan(self) :
        create_person = Person.objects.create(nama="Coba Nama")
        person = Person.objects.get(id=create_person.id)
        kegiatan = Kegiatan.objects.create(nama='Kegiatan 1')
        kegiatan.peserta.add(person)
        count = Kegiatan.objects.count()
        self.assertEqual(count,1)
        self.assertEqual(str(kegiatan), "Kegiatan 1")

    def test_post_method(self) :
        response = self.client.post('/story6/', data={'addKegiatan': "1"})
        self.assertEquals(response.status_code, 302)

        form_kegiatan_data = {'nama' : 'Kegiatan 1'}
        form_kegiatan = KegiatanForm(data=form_kegiatan_data)
        self.assertTrue(form_kegiatan.is_valid())
        kegiatan1 = form_kegiatan.save()
        self.assertEqual(form_kegiatan.save().nama, 'Kegiatan 1')
        self.assertEqual(Kegiatan.objects.count(), 1)
        response2 = self.client.post('/story6/add/', data={'add': "add"})
        self.assertEquals(response.status_code, 302)

        self.assertEqual(Kegiatan.objects.get(id=kegiatan1.id).nama,"Kegiatan 1")

        response3 = self.client.post('/story6/', data={'addPerson': 1})
        form_person_data = {'nama' : 'Rafi'}
        form = PersonForm(data=form_person_data)
        self.assertTrue(form.is_valid())

        response4 = self.client.post('/story6/', data={'addPersonToDatabase': 1})
        person = form.save()
        self.assertEqual(Person.objects.count(), 1)
        Kegiatan.objects.get(id=1).peserta.add(person)
        
        self.assertEqual(Kegiatan.objects.get(id=1).peserta.count(), 1)
        self.assertEquals(response.status_code, 302)


    def test_button_add_kegiatan(self) :
        form_data = {"nama" : "Kegiatan 1"}
        form = KegiatanForm(data=form_data)
        self.assertTrue(form.is_valid())

        form.save()

        response = Client().get('/story6/')
        html_response = response.content.decode('utf8')
        self.assertIn("Kegiatan 1", html_response)

        

    def test_button_add_person(self) :
        Kegiatan.objects.create(nama="Kegiatan1")

        form_data = {'nama' : 'Rafi Muhammad'}
        form = PersonForm(data=form_data)
        self.assertTrue(form.is_valid())
        person = form.save()
        Kegiatan.objects.get(id=1).peserta.add(person)

        response = Client().get('/story6/')
        html_response = response.content.decode('utf8')
        self.assertIn("Rafi Muhammad", html_response)

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

   
