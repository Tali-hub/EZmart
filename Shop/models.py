from django.db import models
from products.models import Product
from django.core.validators import RegexValidator

CATEGORY_CHOICES = (
    ('E', 'Electronics'),
    ('FS', 'Food Stuff'),
    ('T', 'Tools')
)


STORE_STATUSES = (
    ('C', 'Confirmed'),
    ('AC', 'Awaiting confirmation'),
    ('DC','Declined confimation'),
    ('B','Banned'),

)



class StoreManager(models.Manager):

    def __str__(self):
        return self.store_name

class Store(models.Model):
     store_name               = models.CharField( max_length=150)   
     date_joined              = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
     store_address            = models.CharField(max_length=150, default='')
     store_status             = models.CharField(max_length=2,choices = STORE_STATUSES, default='AC')
     businessNum              = models.IntegerField(max_length=14, unique=True )
     store_phone              = models.IntegerField(max_length=14)
     category                 = models.CharField(max_length=3,choices = CATEGORY_CHOICES)
     store_ranking            = models.IntegerField(max_length=1, default=0)
     seller_ID                = models.IntegerField(default= -1)
     products                 = models.ForeignKey(Product,models.SET_NULL, null = True, blank= True) # one store to many products


    #store_socials            = models.ManyToManyField(Social, on_delete=models.CASCADE)  # Store Links to twitter / facebook etc

     object= StoreManager()

