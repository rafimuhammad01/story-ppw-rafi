from django.test import TestCase, Client
from .views import index
# Create your tests here.



class MainTestCase(TestCase):
    def test_url(self) :
        response = Client().get("/story3/")
        response2 = Client().get('/story3/about/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response2.status_code,200)

    def test_template(self) :
        response = Client().get('/story3/')
        html_response = response.content.decode('utf8')
        self.assertIn("Rafi Muhammad", html_response)
        