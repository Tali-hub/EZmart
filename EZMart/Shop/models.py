from django.db import models
from accounts.models import Account
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




    

class Store(models.Model):
    store_name               = models.CharField( max_length=150,unique=True)   
    date_joined              = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    store_address            = models.CharField(max_length=150, default='')
    store_status             = models.CharField(max_length=2,choices = STORE_STATUSES, default='AC')
    businessNum              = models.IntegerField(max_length=14, unique=True )
    store_phone              = models.IntegerField(max_length=14, unique=True )
    category                 = models.CharField(max_length=3,choices = CATEGORY_CHOICES)
    store_ranking            = models.IntegerField(max_length=1, default=0)
    seller                   = models.ForeignKey(Account,  on_delete=models.CASCADE)
    products                 = models.ManyToManyField(Product, on_delete=models.CASCADE)
    #store_socials            = models.ManyToManyField(Social, on_delete=models.CASCADE)  # Store Links to twitter / facebook etc

    
    def __str__(self):
        return self.store_name
    




# # TODO: Organize this shit.
# class MyStoreManager(BaseUserManager):
#     def create_store(self,name,address,businessNum,password= None):
#         if not name:
#             raise ValueError("Store must have a name!")
#         if not address:
#             raise ValueError("Store must have an address!")
#         if not businessNum:
#             raise ValueError("Store must have a BN!")
#         store = self.model(
#             name = name,
#             address = address,
#             businessNum= businessNum
#         )
#         store.set_password(password)
#         store.save(using=self._db)
#         return store

# class Store(AbstractBaseUser):
#     name = models.CharField(
#         max_length=150,
#         validators = [
#             RegexValidator(regex = STORE_NAME_REGEX,
#             message='Store name can only contain alphanumericals, @, #, %, &, * or  numbers',
#             code='invalid_store_name'
#             )],
#          unique=True)
#     date_joined              = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_login               = models.DateTimeField(verbose_name='last login', auto_now=True)
#     store_address            = models.CharField(max_length=150, default='')
#     is_superuser             = models.BooleanField(default=False)
#     is_active                = models.BooleanField(default=False)
#     is_banned                = models.BooleanField(default=False)
#     businessNum              = models.CharField(max_length=14, default='')

#     objects = MyAccManager()
#     USERNAME_FIELD = 'name'
#     REQUIRED_FIELDS = ['name','store_address','businessNum']    

# def __str__(self):
#         return self.name
# def has_perm(self,perm=False,obj=None):
#         return False
# def has_module_perms(self,app_label):
#         return True

"""
    def manage_products(self):
        product_array= models.ManyToManyField(Product, null = True)
        def get_products():
            return product_array
        def addProduct(Product):
            product_array.create(Product)
        
            
"""