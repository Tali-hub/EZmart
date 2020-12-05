from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import Account


def registercustomer(request):
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if len(first_name)<2:
            messages.info(request,'First name to short')
            return redirect('registercustomer')
        if len(last_name)<2:
            messages.info(request,'First name to short')
            return redirect('registercustomer')
        if len(username)<6:
            messages.info(request,'Username to short, should be atleast 6 symbols')
            return redirect('registercustomer')
        if len(address)<6:
            messages.info(request,'Address to short')
            return redirect('registercustomer')
        if len(phone)<8 :
            messages.info(request,'Phone number to short')
            return redirect('registercustomer')
        if len(password1)<6 :
            messages.info(request,'Password to short, should be atleast 6 symbols')
            return redirect('registercustomer')    
        if password1==password2:
            if Account.objects.filter(username=username).exists():
                messages.info(request,'Username is already taken')
                return redirect('registercustomer')
            elif Account.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('registercustomer')
            else:
                user = Account.objects.create_user(
                username=username,
                email=email, 
                first_name=first_name,
                last_name=last_name,
                address=address,
                phone=phone,
                password=password1
            )
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Passwords do not match')
            return redirect('registercustomer')
        
        
    else:
        return render(request, 'registercustomer.html')


    return render(request, 'registercustomer.html') 
        
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')


    else:
        return render(request,'Login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def Cart(request):
    return render(request,'Cart.html')

def Payment(request):
    return render(request,'Payment.html')

def registerbusiness(request):
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        #businesstype = request.POST['businesstype']
        #businessnum = request.POST['businessnum']

        # if len(businessnum)<6:
        #     messages.info(request,'Business number to short')
        #     return redirect('registerbusiness')  
        if len(first_name)<2:
            messages.info(request,'First name to short')
            return redirect('registerbusiness')
        if len(last_name)<2:
            messages.info(request,'First name to short')
            return redirect('registerbusiness')
        if len(username)<6:
            messages.info(request,'Username to short, should be atleast 6 symbols')
            return redirect('registerbusiness')
        if len(address)<6:
            messages.info(request,'Address to short')
            return redirect('registerbusiness')
        if len(phone)<8 :
            messages.info(request,'Phone number to short')
            return redirect('registerbusiness')
        if len(password1)<6 :
            messages.info(request,'Password to short, should be atleast 6 symbols')
            return redirect('registerbusiness')    
        if password1==password2:
            if Account.objects.filter(username=username).exists():
                messages.info(request,'Username is already taken')
                return redirect('registerbusiness')
            elif Account.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('registerbusiness')
            else:
                user = Account.objects.create_business_user(
                email=email, 
                first_name=first_name,
                last_name=last_name,
                address=address,
                phone=phone,
                username=username,
                password=password1,
                #businessType=businesstype
            )
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Passwords do not match')
            return redirect('registerbusiness')
        
        
    else:
        return render(request, 'registerbusiness.html')


    return render(request, 'registerbusiness.html') 


def userProfile(request):    
    #TO-DO - pull username from existing account 
    if request.method == 'POST' :    
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        username = request.GET['username']
        email = request.POST['email']
        address = request.POST['address']
        password = request.POST['password']
        password2 = request.POST['password2']        
        if len(phone)<8 :
            messages.info(request,'Phone number to short')
            return redirect('userProfile')
        if len(password)<6 :
            messages.info(request,'Password to short, should be atleast 6 symbols')
            return redirect('userProfile')    
        if password==password2:           
            if Account.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('userProfile')
            else:    
                user = Account.objects.create_user(
                    username=username,
                    email=email, 
                    first_name=first_name,
                    last_name=last_name,
                    address=address,
                    phone=phone,
                    password=password2
                )
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Passwords do not match')
            return redirect('userProfile')
    else:
        return render(request, 'userProfile.html')