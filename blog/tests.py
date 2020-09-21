from django.test import SimpleTestCase,TestCase
from django.urls import reverse


class HomePageViewTest(TestCase):
    def test_home_page_status_code(self):
        expected = 200
        url = reverse('home')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected, actual)
   
    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        actual = 'home.html'
        self.assertTemplateUsed(response, actual)
    def test_URL_name(self):
        name = reverse('home')
        path = '/'

        self.assertEqual(name, path)