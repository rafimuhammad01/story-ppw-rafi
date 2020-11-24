from django.test import TestCase, Client

# Create your tests here.
class MainTestCase(TestCase):
    def test_url(self) :
        response = Client().get("/story7/")
        self.assertEqual(response.status_code,200)

    def test_template(self) :
        response = Client().get("/story7/")
        self.assertTemplateUsed(response,"story7/index.html")