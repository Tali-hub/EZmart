from django.urls import path
from . import views

urlpatterns = [
   path('register',views.register, name='register'),
  # path('cart', views.Cart, name='cart'),
  # path('payment', views.Payment, name='payment'),
    path('login', views.Login, name='login'),
]
