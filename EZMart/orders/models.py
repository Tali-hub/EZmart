from django.db import models
from accounts.models import Account

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
     object= OrderManager()