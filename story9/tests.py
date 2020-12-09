from django.test import TestCase,Client
from django.contrib.auth.models import User

# Create your tests here.
class MainTestCase(TestCase):
    def test_url(self) :
        response = Client().get("/story9/")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"story9/index.html")

        response = Client().get("/story9/login")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"story9/login.html")

    def test_login(self) :
        user = User.objects.create_user('testing', 'testing@testing.com', 'testing8888')
        response = self.client.post("/story9/login", data={'username' : 'testing', 'password' : 'testing888'})
        self.assertEqual(response.status_code,302)

        response = Client().get("/story9/")
        html_response = response.content.decode('utf8')
        self.assertIn("testing", html_response)
        
    
       


