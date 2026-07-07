from django.contrib import admin
from myrestaurant.models import *

# Register your models here.
@admin.register(User)
class RegisterUser(admin.ModelAdmin):
    list_display=['username','email','role','phone','address','gender','salary','is_active','is_staff','is_superuser','date_joined','password']


@admin.register(Attendance)
class RegisterUser(admin.ModelAdmin):
    list_display=['username','email','role','status','date']



@admin.register(AddItem)
class RegisterUser(admin.ModelAdmin):
    list_display=['item','selling_price','image']
