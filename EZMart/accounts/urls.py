from django.urls import path
from . import views

urlpatterns = [
   path('register1',views.register1, name='register1'),
   path('login', views.Login, name='login'),
   path('cart', views.Cart, name='cart'),
   path('payment', views.Payment, name='payment'),
    
]
