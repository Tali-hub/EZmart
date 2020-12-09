from django.shortcuts import render
from Shop.models import Store
from django.http import HttpResponse,Http404


# Create your views here.
""" def index(request):  
    return render(request, 'index.html') """

def index(request):
        try:
                stores=Store.objects.all()
        except stores.DoesNotExist:
                raise Http404(f'Stores does not exicts')
        # return HttpResponse(f'{store.name} and {store.businessNum}')
        return render(request,'index.html',{'stores':stores})

def register1(request):
        return render(request,'register1.html')

def Login(request):
        return render(request,'Login.html')

def Cart(request):
    return render(request,'Cart.html')

def Payment(request):
    return render(request,'Payment.html')
