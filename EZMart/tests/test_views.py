from django.test import TestCase, Client
from django.urls import reverse
import json
from accounts.models import Account,MyAccManager

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client() # emulate new client

    def test_EZMart_regcust_GET(self):   # test the registercustomer methods

        response = self.client.get(reverse('registercustomer'))  # attempt to get an account by reversing the 'registeredcustomer' functions' path.

        self.assertEquals(response.status_code, 200)  # check if the response was correct using status code: 200
        self.assertTemplateUsed(response, 'registercustomer.html') # check if the corrent template was emulated

    def test_EZMart_regbusi_GET(self):  # test the registerbusiness methods

        response = self.client.get(reverse('registerbusiness'))  # attempt to get an account by reversing the 'registerbusiness' functions' path.

        self.assertEquals(response.status_code, 200)  # check if the response was correct using status code: 200
        self.assertTemplateUsed(response, 'registerbusiness.html') # check if the corrent template was emulated

    def test_EZMart_login_GET(self):  # test the login methods

        response = self.client.get(reverse('login'))  # attempt to get an account by reversing the 'login' functions' path.

        self.assertEquals(response.status_code, 200)  # check if the response was correct using status code: 200
        self.assertTemplateUsed(response, 'Login.html') # check if the corrent template was emulated


    def test_EZMart_cart_GET(self):  # test the cart methods

        response = self.client.get(reverse('cart'))  # attempt to get an account by reversing the 'Cart' functions' path.

        self.assertEquals(response.status_code, 200)  # check if the response was correct using status code: 200
        self.assertTemplateUsed(response, 'Cart.html') # check if the corrent template was emulated

    def test_EZMart_payment_GET(self):  # test the payment methods

        response = self.client.get(reverse('payment'))  # attempt to get an account by reversing the 'Payment' functions' path.

        self.assertEquals(response.status_code, 200)  # check if the response was correct using status code: 200
        self.assertTemplateUsed(response, 'Payment.html') # check if the corrent template was emulated
