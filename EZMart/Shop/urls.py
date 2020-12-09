from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.StoreHomePage, name='StoreHomePage'),
    path('name/<str:name>',views.get_store_by_name),
]