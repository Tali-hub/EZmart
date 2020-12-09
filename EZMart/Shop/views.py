from django.db import transaction
from django.shortcuts import render,redirect
from django.contrib import messages
from products.models import Product


def get_prods(self):
        return Product.objects.filter(store=self)  # make a QuerySet out of the products DB (Matching class Product) wherein the 'store' attribute is equal to this objects (self)
        # the filter used is 'filter' rather than get, as 'get' only supports a single entity be returned, whereas 'filter' returns an "array" (QuerySet)

def manage_prods(self):
        #functionality : show all prods, add new prod, delete prods, update.
        arr_prods = get_prods(self)

        def show_prods():
                print(arr_prods)

        def add_prod(): 
                title=input("product name:")
                price=input("product price:")
                cat=input("Category:\n'E' / 'FS' / 'T'")
                desc=input("product descriptions:")
                quan=input("product quantity:\n")


                newP = Product(
                        title=title,
                        price=price,
                        category=cat,
                        store=self,
                        description=desc,
                        quantity=quan
                        )
                Product.objects.add(newP)
        
        def delete_prod():
                id=input("Enter product ID to delete:\n(NOTE: To update quantity, use 'update' instead")
                arr_prods.get(id=id).delete()

        def update_prod(): #update title / price / quantity
                id=input("Enter product ID to update:\n(NOTE: To delete entirely, use 'delete' instead")
                prod = arr_prods.get(id=id).select_for_update()
                if prod: # ID matched a product in the DB
                        string = input("Enter new title: (leave blank to not change)")
                        flt = input("Enter new price: (leave blank to not change)")
                        quan = input("Update quantity: (leave blank to not change)")
                        if(string is not ""):
                                prod.title= string
                        if(flt is not ""):
                                prod.price= flt
                        if(quan is not ""):
                                prod.quantity= quan
                        prod.save()
                else:
                        print("Sorry, incorrect ID!")


