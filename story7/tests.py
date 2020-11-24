from django.test import TestCase, Client

# Create your tests here.
class MainTestCase(TestCase):
    def test_url(self) :
        response = Client().get("/story7/")
        self.assertEqual(response.status_code,200)

    def test_template(self) :
        response = Client().get("/story7/")
        self.assertTemplateUsed(response,"story7/index.html")

    def test_import_javascript(self) :
        response = Client().get("/story7/")
        html_response = response.content.decode('utf8')
        self.assertIn("scripts.js", html_response)

    def test_html(self) :
        response = Client().get("/story7/")
        html_response = response.content.decode('utf8')
        self.assertIn("What is your name?", html_response)
        self.assertIn("What is this project?", html_response)
        self.assertIn("Can I rearrange the accordion?", html_response)
        self.assertIn("How did you do this?", html_response)

    def test_accordion(self) :
        response = Client().get("/story7/")
        html_response = response.content.decode('utf8')
        self.assertIn("id='accordion'", html_response)

        