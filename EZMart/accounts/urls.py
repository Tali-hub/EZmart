from django.urls import path
from . import views

urlpatterns = [
   path('register',views.register1, name='register'),
   path('login', views.Login, name='login'),
   path('cart', views.Cart, name='cart'),
   path('payment', views.Payment, name='payment'),
    
]
