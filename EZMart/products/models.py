from django.db import models




class OrderedItem(models.Model):
    buyer = models.ForeignKey(Account,  on_delete=models.CASCADE)
    seller = models.ForeignKey(Store,  on_delete=models.CASCADE)
    date_sold = models.DateField()
    price = models.FloatField()

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    #???Shop = models.ManyToManyField(Store)
    #???Buyer = models.ManyToManyField(Account, through= OrderedItem)
    description = models.TextField()
    # slug = models.SlugField()
    
    # image = models.ImageField()

    def __str__(self):
        return self.title

    def set_seller(self, Store):
        if Store is not None:
            self.Shop = Store

    # def get_absolute_url(self):
    #     return reverse("core:product", kwargs={
    #         'slug': self.slug
    #     })

    # def get_add_to_cart_url(self):
    #     return reverse("core:add-to-cart", kwargs={
    #         'slug': self.slug
    #     })

    # def get_remove_from_cart_url(self):
    #     return reverse("core:remove-from-cart", kwargs={
    #         'slug': self.slug
    #     })
