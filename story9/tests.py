from django.test import TestCase,Client

# Create your tests here.
class MainTestCase(TestCase):
    def test_url(self) :
        response = Client().get("/story9/")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"story9/index.html")

        response = Client().get("/story9/login")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"story9/login.html")
        
    
       


