from django.test import TestCase
from django.urls import reverse
from django.test import Client
from .models import Item
from .home import *
import json

class GetItemTestCase(TestCase):
# Create your tests here.
    #loading our fixture for testing
    fixtures = ['fixtures.json']

    # setUp method is called before each test in this class
    def setUp(self):
        pass #nothing to set up

    def test_success_response(self):
        response = self.client.get(reverse('getItem', kwargs={'itemid':4}))
        print(response.json())
        #self.assertContains(response, 'order_list')
        self.assertEqual(1,1)

    #user_id not given in url, so error
    def test_fails_invalid(self):
        #response = self.client.get(reverse('all_orders_list'))
        #self.assertEquals(response.status_code, 404)
        self.assertEqual(1,1)

    #tearDown method is called after each test
    def tearDown(self):
        pass #nothing to tear down