from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import Account


def register(request):
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
            return redirect('register')
        if len(last_name)<2:
            messages.info(request,'First name to short')
            return redirect('register')
        if len(username)<6:
            messages.info(request,'Username to short, should be atleast 6 symbols')
            return redirect('register')
        if len(address)<6:
            messages.info(request,'Address to short')
            return redirect('register')
        if len(phone)<8 :
            messages.info(request,'Phone number to short')
            return redirect('register')
        if len(password1)<6 :
            messages.info(request,'Password to short, should be atleast 6 symbols')
            return redirect('register')    
        if password1==password2:
            if Account.objects.filter(username=username).exists():
                messages.info(request,'Username is already taken')
                return redirect('register')
            elif Account.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            else:
                user = Account.objects.create_user(
                email=email, 
                first_name=first_name,
                last_name=last_name,
                address=address,
                phone=phone,
                username=username,
                password=password1,
                businessNum='None',
                businessType='None',
                store_ID=-1,
                is_business=False
            )
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Passwords do not match')
            return redirect('register')
        
        
    else:
        return render(request, 'register.html')


    return render(request, 'register.html') 
        
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

