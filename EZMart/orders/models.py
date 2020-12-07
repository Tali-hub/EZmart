from django.db import models
from accounts.models import Account
from .utility import unique_order_id_generator


ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
)




class OrderManager(models.Manager):
    def __str__(self):
       return self.product

class OrderedItem(models.Model):
     buyer = models.ForeignKey(Account, models.SET_NULL,blank= True, null= True,related_name="Buyer")  
     seller = models.ForeignKey(Account, models.SET_NULL,blank= True, null= True,related_name="Seller")
     create_date = models.DateTimeField(verbose_name='date_sold',auto_now_add=True)  # updated from "purchase" screen
     price = models.FloatField()
     quantity = models.IntegerField()
     product = models.CharField(max_length= 200)
     status  = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
     shipping_address = models.CharField(max_length = 100)
     objects= OrderManager()
     """class ProductPurchase(models.Model):
     order_id            = models.CharField(max_length=120)
     buyer     = models.ForeignKey(Account)
     product             = models.ForeignKey(Product)
     updated             = models.DateTimeField(auto_now=True)
     timestamp           = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title



        class Order(models.Model):
     billing_profile     = models.ForeignKey(BillingProfile, null=True, blank=True)
     order_id            = models.CharField(max_length=120, blank=True) # AB31DE3
     shipping_address = models.CharField(max_length = 100)
     cart                = models.ForeignKey(Cart)
     status              = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
     shipping_total      = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
     total               = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
     active              = models.BooleanField(default=True)
     updated             = models.DateTimeField(auto_now=True)
     timestamp           = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.order_id

    objects = OrderManager()

    class Meta:
       ordering = ['-timestamp', '-updated']

   def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)



 pre_save.connect(pre_save_create_order_id, sender=Order)
 
"""