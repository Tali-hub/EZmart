from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import  registercustomer, registerbusiness, Login, logout, Cart, Payment  

class TestUrls(SimpleTestCase):

    def test_regcus_url_is_resolved(self):
        url = reverse('registercustomer')  # get the url that matches '/registercustomer' from the 'registercustomer' function in views.py of accounts
        self.assertEqual(resolve(url).func, registercustomer)  # check that the URL is being parsed correctly, and that it is reachable by comparing the .func of it to the imported function
    
    def test_regbusi_url_is_resolved(self):
        url = reverse('registerbusiness')  # get the url that matches '/registerbusiness' from the 'registerbusiness' function in views.py of accounts
        self.assertEqual(resolve(url).func, registerbusiness)  # check that the URL is being parsed correctly, and that it is reachable by comparing the .func of it to the imported function
    
    def test_Login_url_is_resolved(self):
        url = reverse('login')  # get the url that matches '/Login' from the 'Login' function in views.py of accounts
        self.assertEqual(resolve(url).func, Login)  # check that the URL is being parsed correctly, and that it is reachable by comparing the .func of it to the imported function
    
    def test_logout_url_is_resolved(self):
        url = reverse('logout')  # get the url that matches '/logout' from the 'logout' function in views.py of accounts
        self.assertEqual(resolve(url).func, logout)  # check that the URL is being parsed correctly, and that it is reachable by comparing the .func of it to the imported function
    

    def test_cart_url_is_resolved(self):
        url = reverse('cart')  # get the url that matches '/cart' from the 'Cart' function in views.py of accounts
        self.assertEqual(resolve(url).func, Cart)  # check that the URL is being parsed correctly, and that it is reachable by comparing the .func of it to the imported function
    

    def test_payment_url_is_resolved(self):
        url = reverse('payment')  # get the url that matches '/payment' from the 'Payment' function in views.py of accounts
        self.assertEqual(resolve(url).func, Payment)  # check that the URL is being parsed correctly, and that it is reachable by comparing the .func of it to the imported function
    
        