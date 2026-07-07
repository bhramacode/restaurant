from django.shortcuts import render,redirect
from myrestaurant.models import User,Attendance,AddItem
from django.contrib.auth import authenticate,login as login_user,logout as logout_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import *
from django.http import HttpResponse



# dashboard
@login_required(login_url='/login/')
def restaurantDashboard(request):
    return render(request,'dashboard.html',{'username':'admin'})


# take order
@login_required(login_url='/login/')
def takeOrder(request):
    data=AddItem.objects.all()
    context={
        'data':data
    }
        
    return render(request,'take_order.html',context)


# billing
@login_required(login_url='/login/')
def billing(request):
    return render(request,'billing.html')


# kitchen
@login_required(login_url='/login/')
def order(request):
    return render(request,'order.html')


# menu
@login_required(login_url='/login/')
def menu(request):
    data=AddItem.objects.all()
    context={
        'data':data
    }
    return render(request,'menu.html',context)


# staff
@login_required(login_url='/login/')
def staffrecords(request):
    staffs=User.objects.filter(is_superuser=False)
    return render(request,'staffrecords.html',{'staffs':staffs})



# #staff logout
# @login_required(login_url='/login/')
# def stafflogout(request):
#     logout_user(request)
#     return redirect('login')


# delete staff
def deletestaff(request,id):
    get_staff=User.objects.get(id=id)
    get_staff.delete()
    return redirect('staff-records')



# add staff
@login_required(login_url='/login/')
def addstaff(request):
    if request.method=='POST':
        username=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        role=request.POST.get('role')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        salary=request.POST.get('salary')
        staff=request.POST.get('staff')
        superuser=request.POST.get('superuser')
        date=request.POST.get('date')
        
        data=User(
            username=username,
            email=email,
            role=role,
            address=address,
            phone=phone,
            salary=salary,
            date_joined=date
            )
        data.set_password(password)
        
        if staff == 'staff':
            data.is_staff=True
        elif superuser == 'admin':
            data.is_superuser=True
            data.is_staff=True
            
        data.save()
        return redirect('add-staff')
        
    return render(request,'addstaff.html')


# admin/staff login
def login(request):
    if request.method == 'POST':
        userName = request.POST.get('username')
        password = request.POST.get('password')
        
        errors = {}

        if not userName:
            errors['name_error'] = 'Username required'
        
        if not password:
            errors['password_error'] = 'Password required'
        
        if errors:
            return render(request, 'login.html', {'error': errors})
        
        user = authenticate(request, username=userName, password=password)
        
        if user is not None:
            if user.is_superuser :
                login_user(request, user)
                return redirect('dashboard')
        
            if not user.is_superuser:
                return HttpResponse("welcome staff")
        else:
            return render(request, 'login.html', {
                'credential_error': "Invalid username or password"
            })

    return render(request, 'login.html')


# admin logout
@login_required(login_url='/login/')
def logout(request):
    logout_user(request)
    return redirect('login')



# stock
@login_required(login_url='/login/')
def stock(request):
    return render(request,'stock.html')



# staff attendance
@login_required(login_url='/login/')
def savestaffattendance(request):     
    get_staff=User.objects.filter(is_superuser=False)
    
    if request.method=='POST':
        name=request.POST.get('select-staff')
        email=request.POST.get('email')
        role=request.POST.get('role')
        status=request.POST.get('attendance')
        date=request.POST.get('date')
        
        errors={}
        if not name:
            errors['name_error']="name required"
            
        if not email:
            errors['email_error']="email required"
        
        if not role:
            errors['role_error']="role required"
        
        if not status:
            errors['status_error']="status required"
            
        if not date:
            errors['date_error']="date required"
        
        if errors:
            return render(request,'staffattendance.html',{'errors':errors})
        
        
        data=Attendance(username=name,email=email,role=role,status=status,date=date)
        data.save()
        return render(request,'staffattendance.html',context={'success':"submitted"})
    return render(request,'staffattendance.html',{'staffs':get_staff})
    


# cart
@login_required(login_url='/login/')
def cart(request):
    return render(request,'cart.html')



# add item
@login_required(login_url='/login/')
def additem(request):
    if request.method=='POST':
        item=request.POST.get('item')
        sp=request.POST.get('selling-price')
        image=request.FILES.get('image-file')
        
        errors={}
        
        if not item:
            errors['item_error']="item name is required"
            
        
        if not sp:
            errors['sp_error']="selling price is required"
            
        
        if not cp:
            errors['cp_error']="cost price is required"
            
        
        if not stock:
            errors['stock_error']="stock is required"
            
        if not image:
            errors['image_error']="image is required"
            
        if errors:
            return render(request,'additem.html',{'error':errors})
        
        get_data=AddItem(item=item,selling_price=sp,cost_price=cp,stock=stock,image=image)
        get_data.save()
        
        return render(request,'additem.html',context={'success':'added item'})
    return render(request,'additem.html')


# staff attendance records
@login_required(login_url='/login/')
def staffattendancerecords(request):
    get_staff=Attendance.objects.all()
    return render(request,'staffattendancerecords.html',{'attendances':get_staff})



# delete attendance
def deleteattendance(request,id):
    get_staff=Attendance.objects.get(id=id)
    get_staff.delete()
    return redirect('attendancerecords')

