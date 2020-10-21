from django.test import TestCase, Client
from .views import index
# Create your tests here.



class MainTestCase(TestCase):
    def test_url(self) :
        response = Client().get("/")
        self.assertEqual(response.status_code,302)

    def test_template(self) :
        pass
        