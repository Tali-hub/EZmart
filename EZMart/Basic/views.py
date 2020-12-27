from django.shortcuts import render, redirect
from products.models import Product
from django.http import HttpResponse, Http404
from .models import Form
from django.contrib import messages
from django.views.generic.list import ListView

def index(request):
    allProducts = Product.objects.all()
    products = {'allProducts':allProducts}
    return render(request, 'index.html', products)


def register1(request):
    return render(request, 'register1.html')


def Login(request):
    return render(request, 'Login.html')


def Payment(request):
    return render(request, 'Payment.html')

def aboutUs(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        new_form = Form(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        new_form.save()
        messages.info(request, 'Your message successfully sent')
        return redirect('contact')
    else:
        return render(request, 'contact.html')


class SearchProdView(ListView):
    model = Product
    template_name = 'search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchProdView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Product.objects.filter(quantity__gte=1).filter(store__status='C').filter(title__contains=query)
          result = postresult
       else: 
            result = Product.objects.filter(quantity__gte=1).filter(store__status='C')
       return result

def purchase (request):
    return render(request, 'purchase.html')
