from django.test import TestCase
from django.urls import reverse
from django.test import Client

# Create your tests here.
class CurrencyTestClass(TestCase):
    def setUp(self):
       self.client = Client()
    def test_home_not_404(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def dollar_in_home(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '$')