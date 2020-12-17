from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Store
from products.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,Http404
from accounts.models import Account
from django.core.files.storage import FileSystemStorage
def StoreHomePage(request):  
    return render(request, 'StoreHomePage.html')



def get_store_by_name(request,name):
        try:
                store=Store.objects.get(name=name)
        except store.DoesNotExist:
                raise Http404(f'Store {name} does not exicts')
        # return HttpResponse(f'{store.name} and {store.businessNum}')
        return render(request,'StoreHomePage.html',{'store':store})
def get_prods(self):# helper queryset func
        return Product.objects.filter(store=self)  # make a QuerySet out of the products DB (Matching class Product) wherein the 'store' attribute is equal to this objects (self)
        # the filter used is 'filter' rather than get, as 'get' only supports a single entity be returned, whereas 'filter' returns an "array" (QuerySet)

######################### STORE API #################################

def show_prods(self): 
        print(get_prods(self))

def add_prod(request):
        if request.method == 'POST':
                user  = request.user.username 
                user  = Account.objects.get(username = user) 
                name  = request.POST.get('name')
                price = float(request.POST.get('price'))
                cat   = request.POST.get('category')
                desc  = request.POST.get('desc')
                quan  = int(request.POST.get('quantity'))
                pic   = request.FILES['myfile'] if 'myfile' in request.FILES else False
                newP = Product(
                        title=name,
                        price=price,
                        quantity=quan,
                        category=cat,
                        description=desc,
                        )
                if(pic != False):
                        fs = FileSystemStorage("static/images")
                        fs.save(pic.name,pic)
                        fileurl ="static/images" + fs.url(pic)       
                        newP.img = fileurl
                newP.store = user.store
                newP.save()
                return redirect('inventory')
        else:
                return render(request,'inventory.html')


def delete_prod(self):
        title=input("Enter name of product to delete:\n(NOTE: To update, use 'update' instead)\n")
        try:
                get_prods(self).get(title=title).delete()
        except ObjectDoesNotExist:
                print("No object matching that ID was found!")

def update_prod(self): #update title / price / quantity
        title=input("Enter name of product to update:\n(NOTE: To delete entirely, use 'delete' instead)\n")
        try:
                prod = get_prods(self).get(title=title)
                string = input("Enter new title: (leave blank to not change)")
                flt = input("Enter new price: (leave blank to not change)")
                quan = input("Update quantity: (leave blank to not change)")
                if(string is not ""):
                        prod.title= string
                if(flt is not "" and flt >= 0):
                        prod.price= flt
                if(quan is not "" and quan >= 0):
                        prod.quantity= quan
                prod.save()
        except ObjectDoesNotExist:
                print("Sorry, incorrect ID!")


def inventory(request):       

        

    return render(request,'inventory.html')

