from django.shortcuts import render,redirect
from Shop.models import Store
from django.http import HttpResponse,Http404
from .models import Form
from django.contrib import messages



def index(request):
        try:
                stores=Store.objects.filter(status='C')
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
        messages.info(request,'Your message successfully sent')
        return redirect('contact')
    else:
        return render(request, 'contact.html')
