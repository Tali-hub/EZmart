from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.validators import RegexValidator
import Shop


USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'
STORE_NAME_REGEX = '^[A-Za-z0-9!@#$%^&* ]*$'

<<<<<<< Updated upstream
=======

ACCOUNT_TYPES = (
        ('A', 'Admin'),
        ('B', 'Business'),
        ('C', 'Customer'),
    )


>>>>>>> Stashed changes
class MyAccManager(BaseUserManager):
    def create_user(self,username,email,first_name,last_name,address,phone,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        user = self.model(
            username = username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,email,password=None):
        user = self.create_user(
            username = username,
            email=self.normalize_email(email),
            first_name='Admin',
            last_name='Admin',
            address='',
            phone='',
            password = password,
           
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True 
        user.save(using=self._db)
        return user
    def create_business_user(self,email,first_name,last_name,address,phone,username,businessType,password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone,
            password = password
        )
        user.is_business=True
        user.businessType=businessType
        # Func in future to set up business ID
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username                    = models.CharField(
        max_length=300,
        validators = [
            RegexValidator(regex = USERNAME_REGEX,
            message='Username must be alphanumeric or contain numbers',
            code='invalid_username'
            )],
         unique=True)
    email                    = models.EmailField(max_length=255,unique=True,verbose_name="email address")
    data_joined              = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login               = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin                 = models.BooleanField(default=False)
    is_active                = models.BooleanField(default=True)
    is_staff                 = models.BooleanField(default=False)
    is_superuser             = models.BooleanField(default=False)
    first_name               = models.CharField(max_length=30, default='')
    last_name                = models.CharField(max_length=30, default='')
    address                  = models.CharField(max_length=150, default='')
    phone                    = models.CharField(max_length=14, default='')
    businessType             = models.CharField(max_length=30, default='')
    store_ID                 = models.IntegerField(default=-1)
    is_business              = models.BooleanField(default=False)    

    objects = MyAccManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    





# TODO: Organize this shit.
class MyStoreManager(BaseUserManager):
    def create_store(self,name,address,businessNum,password= None):
        if not name:
            raise ValueError("Store must have a name!")
        if not address:
            raise ValueError("Store must have an address!")
        if not businessNum:
            raise ValueError("Store must have a BN!")
        store = self.model(
            name = name,
            address = address,
            businessNum= businessNum
        )
        store.set_password(password)
        store.save(using=self._db)
        return store

class Store(AbstractBaseUser):
    name = models.CharField(
        max_length=150,
        validators = [
            RegexValidator(regex = STORE_NAME_REGEX,
            message='Store name can only contain alphanumericals, @, #, %, &, * or  numbers',
            code='invalid_store_name'
            )],
         unique=True)
    date_joined              = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login               = models.DateTimeField(verbose_name='last login', auto_now=True)
    store_address            = models.CharField(max_length=150, default='')
    is_superuser             = models.BooleanField(default=False)
    is_active                = models.BooleanField(default=False)
    is_banned                = models.BooleanField(default=False)
    businessNum              = models.CharField(max_length=14, default='')

    objects = MyAccManager()
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['name','store_address','businessNum']    

def __str__(self):
        return self.name
def has_perm(self,perm=False,obj=None):
        return False
def has_module_perms(self,app_label):
        return True

"""
    def manage_products(self):
        product_array= models.ManyToManyField(Product, null = True)
        def get_products():
            return product_array
        def addProduct(Product):
            product_array.create(Product)
        
            

class OrderedItem(models.Model):
    buyer = models.ForeignKey(Account,  on_delete=models.CASCADE)
    seller = models.ForeignKey(Store,  on_delete=models.CASCADE)
    date_sold = models.DateField()
    price = models.FloatField()

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    Shop = models.ManyToManyField(Store, null= True)
    Buyer = models.ManyToManyField(Account, through= OrderedItem)
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
"""
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
