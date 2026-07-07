from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from myrestaurant.managers import CustomManager
from django.utils import timezone

#all staff(admin/staff)
class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=100,blank=False,unique=True)
    email=models.EmailField(max_length=254,unique=True,blank=True,null=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    address=models.TextField(blank=True,null=True)
    phone=models.CharField(max_length=10,blank=True,null=True)
    gender=models.CharField(max_length=6,blank=True,null=True)
    role=models.CharField(max_length=100,blank=True,null=True)
    salary=models.BigIntegerField(blank=True,null=True)
    date_joined=models.DateTimeField(default=timezone.now)
  
    
    
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]
    objects=CustomManager()
    def __str__(self):
        return self.username


# attendance
class Attendance(models.Model):
    username=models.CharField(max_length=100,blank=False,unique=True)
    email=models.EmailField(max_length=254,unique=True,blank=True,null=True)
    role=models.CharField(max_length=100,blank=True,null=True)
    status=models.CharField(max_length=20)
    date=models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.username
  
    
# add item
class AddItem(models.Model):
    item=models.TextField(blank=False)
    selling_price=models.TextField(blank=False)
    image=models.ImageField()
    
    def __str__(self):
        return self.item
  
    
    
