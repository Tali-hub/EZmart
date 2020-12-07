from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Store






# def add_store(acc, businum):
#         new_store = Store(
#                 store_name= "",
#                 businessNum = businum,
#                 seller = acc
#         )
#         new_store.save()
#         acc.store= new_store
#         return acc


        #store_name               = models.CharField( max_length=150,unique=True)   
#     date_joined              = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     store_address            = models.CharField(max_length=150, default='')
#     store_status             = models.CharField(max_length=2,choices = STORE_STATUSES, default='AC')
#     businessNum              = models.IntegerField(max_length=14, unique=True )
#     store_phone              = models.IntegerField(max_length=14, unique=True )
#     category                 = models.CharField(max_length=3,choices = CATEGORY_CHOICES)
#     store_ranking            = models.IntegerField(max_length=1, default=0)
#     seller      
#if request.method == 'POST' :
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # username = request.POST['username']
# # def manage_products(self):
# #     def get_products():
# #             return self.products
# #     def addProduct(Product):
# #             self.products.add(Product)