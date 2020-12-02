from django.test import TestCase,Client

# Create your tests here.

class MainTestCase(TestCase):
    def test_url(self) :
        response = Client().get("/story8/")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"story8/index.html")

    def test_url_data(self) :
        response = Client().get("/story8/data")
        self.assertEqual(response.status_code,200)

    def test_search_bar(self) :
        response = Client().get("/story8/")
        html_response = response.content.decode('utf8')
        self.assertIn("input", html_response)


    