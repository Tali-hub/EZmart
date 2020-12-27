from django.db import models
from accounts.models import Account


class OrderManager(models.Manager):
    def __str__(self):
        return self.product


class OrderedItem(models.Model):
    buyer = models.CharField(max_length=200, null=True)
    seller = models.CharField(max_length=200,  null=True)
    # updated from "purchase" screen
    create_date = models.DateTimeField(
        verbose_name='date_sold', auto_now_add=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    product = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=100)
    object = OrderManager()
