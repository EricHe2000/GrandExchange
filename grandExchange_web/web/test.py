from django.test import TestCase
from django.urls import reverse
from django.test import Client
import re
# Create your tests here.
class CurrencyTestClass(TestCase):
    def setUp(self):
        pass
    def test_home_not_404(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_dollar_in_home(self):
        response = self.client.get(reverse('home'))
        html = response.content.decode('utf8')
        # print (html)
        # response = self.client.get(reverse('detail'))
        # self.assertContains(html, 'Price: \d*\.?\d{2}g')
        x = re.search('Price: \d*\.?\d{2}g', html)
        if x:
            y = True
        else:
            y=False
        self.assertTrue(y)
    def test_dollar_in_detail(self):
        response = self.client.get(reverse('detail', args = [1]))
        html = response.content.decode('utf8')
        # self.assertContains(response, 'Price: \d*\.?\d{2}g')
        x = re.search('Price: \d*\.?\d{2}g', html)
        if x:
            y = True
        else:
            y=False
        self.assertTrue(y)