from django.shortcuts import render, redirect
from products.models import Product
from accounts.models import Account
from django.core.mail import send_mail

def show_product(request):
    try:
        products = Product.objects.filter(quantity__gte=1).filter(store__status='C')
        context = {'products': products}
        return render(request, 'product.html', context)
    except:
        return render(request, 'product.html')

def buy_product(request,id):
    product = Product.objects.get(id=id)
    # if product.quantity > 0:  TODO: SEND TO CHECKOUT BUTTON
    #    product.quantity -= 1
    # product.save()
    user = Account.objects.get(store = product.store)
    email = user.email

    #notify seller of purchase
    send_mail(
    'New Order!',
    'You have one new order awaiting you in your EZMart shop!\nAddress: {user.address}\nProduct: {product.title}\nPhone:{user.phone}',
    'EZMartSCE@gmail.com',
    [email],
    fail_silently=False,
)
