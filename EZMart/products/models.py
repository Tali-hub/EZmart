from django.db import models
from Shop.models import Store


CATEGORY_CHOICES = (
    ('E', 'Electronics'),
    ('FS', 'Food Stuff'),
    ('T', 'Tools')
)




class ProductManager(models.Manager):
    def __str__(self):
        return self.title

#     # def get_absolute_url(self):
#     #     return reverse("core:product", kwargs={
#     #         'slug': self.slug
#     #     })



class Product(models.Model):
    title = models.CharField(max_length=100, default ='Product name here')
    price = models.FloatField(default=0)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    store = models.ForeignKey(Store, models.SET_NULL,blank= True, null= True)
    description = models.CharField(max_length=200 , default ='Description name here')
    active = models.BooleanField(default= True)
    time_stamp= models.DateTimeField(verbose_name="Time Stamp",auto_now=True)

    object = ProductManager()
    # slug = models.SlugField()
    # image = models.ImageField()






   