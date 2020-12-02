from django.urls import path
from . import views

urlpatterns = [
   path('registercustomer',views.registercustomer, name='registercustomer'),
   path('cart', views.Cart, name='cart'),
   path('payment', views.Payment, name='payment'),
   path('login', views.Login, name='login'),
	path("logout",views.logout, name="logout"),
   path('registerbusiness',views.registerbusiness, name='registerbusiness'),
   path('userProfile',views.userProfile, name='userProfile'),
]
