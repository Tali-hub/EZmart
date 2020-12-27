from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.aboutUs, name='about'),
    path('search', views.SearchProdView.as_view(), name='search'),
    path('purchase', views.purchase, name='purchase'),
    path('checkout', views.checkout, name='checkout'),
    
]
