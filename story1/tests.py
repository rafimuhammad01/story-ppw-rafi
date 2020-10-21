from django.test import TestCase, Client
from .views import index
# Create your tests here.



class MainTestCase(TestCase):
    def test_url(self) :
        response = Client().get("/story1/")
        self.assertEqual(response.status_code,200)

    def test_template(self) :
        response = Client().get('/story1/')
        html_response = response.content.decode('utf8')
        self.assertIn("Universitas Indonesia", html_response)
        self.assertIn("Rafi Muhammad", html_response)
        
   
