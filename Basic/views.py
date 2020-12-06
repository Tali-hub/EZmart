from django.shortcuts import render

# Create your views here.
def index(request):  
    return render(request, 'index.html')

def register1(request):
        return render(request,'register1.html')

def Login(request):
        return render(request,'Login.html')

def Cart(request):
    return render(request,'Cart.html')

def Payment(request):
    return render(request,'Payment.html')
