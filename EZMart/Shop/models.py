from django.db import models
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
        return self.name

class Store(models.Model):
     name               = models.CharField( max_length=150,default='Store Name')   
     date_joined        = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
     address            = models.CharField(max_length=150, default='Store Address')
     status             = models.CharField(max_length=2,choices = STORE_STATUSES, default='AC')
     businessNum        = models.IntegerField(unique=True )
     phone              = models.IntegerField(default=0)
     category           = models.CharField(max_length=3,choices = CATEGORY_CHOICES)
     ranking            = models.IntegerField(default=0)
    #store_socials            = models.ManyToManyField(Social, on_delete=models.CASCADE)  # Store Links to twitter / facebook etc

     object= StoreManager()

