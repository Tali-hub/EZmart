from django.db import models



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
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    shop_id = models.IntegerField(default = -1)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default= True)
    time_stamp= models.DateTimeField(verbose_name="Time Stamp",auto_now_add=True)

    object = ProductManager()
    # slug = models.SlugField()
    # image = models.ImageField()






   