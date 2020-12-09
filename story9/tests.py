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
        response = self.client.post("/story9/login", data={'username' : 'testing', 'password' : 'testing8888', 'login':"login"}, follow=True)
        self.assertEqual(response.status_code,200)

        html_response = response.content.decode('utf8')
        self.assertIn('testing', html_response)

    def test_register_url(self) :
        response = Client().get("/story9/signup")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"story9/signup.html")
    
    def test_register(self) :
        response = self.client.post("/story9/signup", data={'username' : 'testing', 'password1' : 'testing8888','password2' : 'testing8888', 'signup':"signup"}, follow=True)
        self.assertEqual(1, User.objects.count())
    
       


