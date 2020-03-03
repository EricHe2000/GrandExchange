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

    #checks to see if it returns the correct item
    def test_success_response(self):
        item_id = 4
        response = self.client.get(reverse('getItem', kwargs={'itemid':item_id}))
        value = response.json()
        self.assertEqual(value['id'], item_id)

    #returns good error message when no item is found
    def test_fails_invalid(self):
        item_id = 999
        response = self.client.get(reverse('getItem', kwargs={'itemid':item_id}))
        value = response.json()
        self.assertEqual(value['Error'], 'Item does not exist')

    #tearDown method is called after each test
    def tearDown(self):
        pass #nothing to tear down



class GetHottestItemsTestCase(TestCase):
    # Create your tests here.
    # loading our fixture for testing
    fixtures = ['fixtures.json']

    # setUp method is called before each test in this class
    def setUp(self):
        pass  # nothing to set up

    # checks to see if it returns the correct item
    def test_success_response(self):
        hot_item = "Rune scimitar"
        response = self.client.get(reverse('getHottestItem'))
        value = response.json()
        self.assertEqual(value[0]['title'], hot_item)

    # returns good error message when no item is found
    def test_fails_invalid(self):
        second_hot_item = "Yew logs"
        response = self.client.get(reverse('getHottestItem'))
        value = response.json()
        self.assertEqual(value[1]['title'], second_hot_item)

    # tearDown method is called after each test
    def tearDown(self):
        pass  # nothing to tear down


class GetCheapestItemsTestCase(TestCase):
    # Create your tests here.
    # loading our fixture for testing
    fixtures = ['fixtures.json']

    # setUp method is called before each test in this class
    def setUp(self):
        pass  # nothing to set up

    # checks to see if it returns the correct item
    def test_success_response(self):
        cheap_item = "12.00"
        response = self.client.get(reverse('getCheapestItem'))
        value = response.json()
        self.assertEqual(value[0]['price'], cheap_item)

    # tearDown method is called after each test
    def tearDown(self):
        pass  # nothing to tear down

class DeleteItemTestCase(TestCase):
    # Create your tests here.
    # loading our fixture for testing
    fixtures = ['fixtures.json']

    # setUp method is called before each test in this class
    def setUp(self):
        pass  # nothing to set up

    # checks to see if it returns the correct item
    def test_success_response(self):

        item_id = 2

        response = self.client.get(reverse('deleteItem', kwargs={'itemid':item_id}))
        value = response.json()
        self.assertEqual(value['Success'], 'Your item has been deleted.')

    # tearDown method is called after each test
    def tearDown(self):
        pass  # nothing to tear down