from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from .views import index
from .models import MataKuliah
# Create your tests here.



class MainTestCase(TestCase):
    def test_url(self) :
        MataKuliah.objects.create(nama_matkul="PPW", semester="3", deskripsi="tes11223", sks="4")

        response = Client().get("/story5/")
        response2 = Client().get('/story5/add/')
        response3 = Client().get('/story5/update/1')
        response4 = Client().get('/story5/detail/1')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response2.status_code,200)
        self.assertEqual(response3.status_code,200)
        self.assertEqual(response4.status_code,200)
        self.assertEqual(str(MataKuliah.objects.get(id=1)),'PPW')

    def test_template(self) :
        response = Client().get('/story5/')
        html_response = response.content.decode('utf8')
        self.assertIn("Daftar Mata Kuliah", html_response)

    def test_post_method_index(self) :
        response = self.client.post('/story5/', data={'add' : 'add'})
        self.assertEqual(response.status_code, 302)

    def test_post_method_detail(self) :
        MataKuliah.objects.create(nama_matkul="PPW", semester="3", deskripsi="tes11223", sks="4")
        response = self.client.post('/story5/detail/1', data={'update' : 1})
        self.assertEqual(response.status_code, 302)

        response2 = self.client.post('/story5/detail/1', data={'delete' : 1})
        self.assertEqual(MataKuliah.objects.count(), 0)
        self.assertEqual(response.status_code, 302)

    def test_form_add(self) :
        response = self.client.post('/story5/add/', data={'nama_matkul' : 'PPW', "semester" : "3", "deskripsi" : "tes123", "sks": "4"})
        self.assertEqual(MataKuliah.objects.count(), 1)

    def test_form_update(self) :
        MataKuliah.objects.create(nama_matkul="PPW", semester="3", deskripsi="tes11223", sks="4")
        response = self.client.post('/story5/update/1', data={'nama_matkul' : 'PPW2', "semester" : "3", "deskripsi" : "tes123", "sks": "4"})
        self.assertEqual(MataKuliah.objects.get(id=1).nama_matkul, "PPW2")