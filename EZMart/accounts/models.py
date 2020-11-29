from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class MyAccManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,address,phone,username,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not address :
            raise ValueError("Users must have a address")
        if not phone:
            raise ValueError("Users must have a phone number")
        user = self.model(
            email=self.normalize_email(email),
            username = username,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone
        )
        user.set_password(password)
        user.save(user=self._db)
        return user
    def create_superuser(self,email,first_name,last_name,address,phone,username,password):
        user = self.model(
            email=self.normalize_email(email),
            username = username,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    email                    = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username                 = models.CharField(max_length=30,unique=True)
    data_joined              = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login               = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin                 = models.BooleanField(default=False)
    is_active                = models.BooleanField(default=True)
    is_staff                 = models.BooleanField(default=False) # a admin user; non super-user
    first_name               = models.CharField(max_length=30)
    last_name                = models.CharField(max_length=30)
    address                  = models.CharField(max_length=150)
    phone                    = models.CharField(max_length=14)
    businessNum              = models.CharField(max_length=14, default=None)
    businessType             = models.CharField(max_length=30, default=None)
    store_ID                 = models.CharField(max_length=30, default=None)
    is_business              = models.BooleanField(default=False)    


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email','first_name','last_name','Address','Phone','username']
    def __str__(self):
        return self.username
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
    