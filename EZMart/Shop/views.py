from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Store
from products.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,Http404

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

def add_prod(self): 
        title=input("product name:")
        price=float(input("product price:"))
        cat=input("Category:\n'E' / 'FS' / 'T'\n")
        desc=input("product descriptions:")
        quan=int(input("product quantity:\n"))


        newP = Product(
                title=title,
                price=price,
                category=cat,
                store=self,
                description=desc,
                quantity=quan
                )
        newP.save()

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



