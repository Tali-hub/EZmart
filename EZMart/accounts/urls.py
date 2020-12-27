from django.urls import path,include
from . import views

urlpatterns = [
   path('registercustomer',views.registercustomer, name='registercustomer'),
   path('payment', views.Payment, name='payment'),
   path('login', views.Login, name='login'),
	path("logout",views.logout, name="logout"),
   path('registerbusiness',views.registerbusiness, name='registerbusiness'),
   path('userProfile',views.userProfile, name='userProfile'),
   path('businessProfile',views.businessProfile, name='businessProfile'),
   
]
