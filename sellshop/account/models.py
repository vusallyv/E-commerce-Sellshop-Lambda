from django.db import models
from django.contrib.auth.models import AbstractUser
from sellshop.utils.base_models import BaseModel


class User(AbstractUser):
    first_name = models.CharField(verbose_name='first_name', max_length=255, null=False, blank=False, default="")
    last_name = models.CharField(verbose_name='last_name', max_length=255, null=False, blank=False, default="")
    email = models.EmailField(verbose_name="Email Address", null=False, blank=False, default="")
    
    def __str__(self):
        return f"{self.email}"
      

class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    country = models.CharField(verbose_name="Country", max_length=255, null=True, blank=True, default="")
    address = models.CharField(verbose_name="Address", max_length=255, null=True, blank=True, default="")
    city = models.CharField(verbose_name="City", max_length=30, null=True, blank=True, default="")
    phone_number = models.CharField(verbose_name="Phone number",max_length=255, null=True, blank=True, default=""'')
    additional_info = models.TextField(verbose_name="Additional Info", default="", null=True, blank=True) 
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        
    def __str__(self):
        return f'{self.user} - Profile'
        
    

class Contact(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    email = models.EmailField(verbose_name="Email", null=False, blank=False, default="")
    message = models.CharField(max_length=1000,verbose_name="Message")

    def __str__(self):
        return self.name
    

