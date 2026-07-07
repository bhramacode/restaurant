from django.urls import path
from myrestaurant.views import *


urlpatterns = [
    path('',login,name='login'),
    path('dashboard/',restaurantDashboard,name='dashboard'),
    path('take-order/',takeOrder,name='take-order'),
    path('billing/',billing,name='billing'),
    path('order/',order,name='order'),
    path('menu/',menu,name='menu'),
    path('staff-records/',staffrecords,name='staff-records'),
    path('add-staff/',addstaff,name='add-staff'),
    path('save-staff-attendance/',savestaffattendance,name='save-staff-attendance'),
    path('stock/',stock,name='stock'),
    path('logout/',logout,name='logout'),
    path('delete-staff/<int:id>/',deletestaff,name='deletestaff'),
    path('cart/',cart,name='cart'),
    path('add-item/',additem,name="add-item"),
    path('attendance-records/',staffattendancerecords,name='attendancerecords'),
    path('delete-attendance/<int:id>/',deleteattendance,name='deleteattendance'),
    
    
]
