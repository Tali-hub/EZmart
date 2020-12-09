from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import Account
from Shop.models import Store
from django.contrib.auth.decorators import login_required






def registercustomer(request):
    if(request.user.is_authenticated):
        return redirect('/')
    if request.method == 'POST':
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
    if(request.user.is_authenticated):
        return redirect('/')
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

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

def Cart(request):
    return render(request,'Cart.html')

def Payment(request):
    return render(request,'Payment.html')

def registerbusiness(request):
    if(request.user.is_authenticated):
        return redirect('/')
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        businessnum = request.POST['businessnum']

        if len(businessnum)<6:
            messages.info(request,'Business number to short')
            return redirect('registerbusiness')  
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
                store1 = Store(
                    businessNum = int(businessnum)
                )
                user = Account.objects.create_business_user(
                email=email, 
                first_name=first_name,
                last_name=last_name,
                address=address,
                phone=phone,
                username=username,
                password=password1,
            )   
                store1.save()
                user.store = store1
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Passwords do not match')
            return redirect('registerbusiness')
        
        
    else:
        return render(request, 'registerbusiness.html')


    return render(request, 'registerbusiness.html') 

@login_required(login_url='login')
def userProfile(request):     
    user=request.user.username 
    u = Account.objects.get(username = user)   
    if u.acc_type == 'B':
       return redirect('businessProfile') 
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        cur_password=request.POST['cur_password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if  u is not None and u.check_password(cur_password): 
            if password1==password2:
                if Account.objects.filter(email=email).exists():
                    messages.info(request,'Email already exists')
                    return redirect('userProfile')
                else:
                    flag= False
                if first_name != '':
                    u.first_name = first_name
                    flag= True
                if last_name != '':
                    u.last_name = last_name
                    flag= True
                if phone != '':
                    u.phone = phone                    
                    if len(phone)<8 :
                        messages.info(request,'Phone number to short')
                        return redirect('userProfile') 
                    else:
                        u.phone=phone
                        flag= True                      
                if email != '':
                    u.email = email
                    flag= True
                if address != '':
                    u.address = address
                    flag= True           
                if password1 != '':
                    if len(password1)<6 :
                        messages.info(request,'Password to short, should be atleast 6 symbols')                        
                        return redirect('userProfile')
                    else:
                        flag= True
                        u.set_password(password1)                        
                if flag: 
                    u.save()
                return redirect('userProfile')

            else:
                messages.info(request,'Passwords do not match')
                return redirect('userProfile')
        else:
            messages.info(request,'Current Password do not match')
            return redirect('userProfile')
    else:
        return render(request, 'userProfile.html')


@login_required(login_url='login')
def businessProfile(request):
    user=request.user.username 
    u = Account.objects.get(username = user)   
    if u.acc_type != 'B':
       return redirect('userProfile')
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        cur_password=request.POST['cur_password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if  u is not None and u.check_password(cur_password):
            if password1==password2:
                if Account.objects.filter(email=email).exists():
                    messages.info(request,'Email already exists')
                    return redirect('businessProfile')
                else:
                    flag= False
                if first_name != '':
                    u.first_name = first_name
                    flag= True
                if last_name != '':
                    u.last_name = last_name
                    flag= True
                if phone != '':
                    u.phone = phone                    
                    if len(phone)<8 :
                        messages.info(request,'Phone number to short')
                        return redirect('businessProfile') 
                    else:
                        u.phone=phone
                        flag= True                      
                if email != '':
                    u.email = email
                    flag= True
                if address != '':
                    u.address = address
                    flag= True           
                if password1 != '':
                    if len(password1)<6 :
                        messages.info(request,'Password to short, should be atleast 6 symbols')
                        
                        return redirect('businessProfile')
                    else:
                        flag= True
                        u.set_password(password1)                        
                if flag: 
                    u.save()
                return redirect('businessProfile')

            else:
                messages.info(request,'Passwords do not match')
                return redirect('businessProfile')
        else:
            messages.info(request,'Current Password do not match')
            return redirect('businessProfile')
    else:
        return render(request, 'businessProfile.html')