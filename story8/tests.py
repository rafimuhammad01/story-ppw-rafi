from django.test import TestCase

# Create your tests here.

class MainTestCase(TestCase):
    def test_url(self) :
        response = Client().get("/story8/")
        self.assertEqual(response.status_code,200)

    def test_url_data(self) :
        response = Client().get("/story8/data")
        self.assertEqual(response.status_code,200)