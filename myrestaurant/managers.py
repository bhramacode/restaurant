from django.contrib.auth.models import BaseUserManager

class CustomManager(BaseUserManager):
    def create_user(self,username,password=None,**extra_fields):
        if not username:
            raise ValueError("username should not be empty")

        email=extra_fields.get('email')
        if email:
            extra_fields['email']=self.normalize_email(email)
        else:
            extra_fields['email']=None
            
        user=self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self,username,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("is_staff should be true")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("is_superuser should be true")
        
        return self.create_user(username,password,**extra_fields)
        