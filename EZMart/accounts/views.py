from django.shortcuts import render

def register1(request):

    return render(request, 'register1.html')     

def Login(request):
        return render(request,'Login.html')

def Cart(request):
    return render(request,'Cart.html')

def Payment(request):
    return render(request,'Payment.html')
