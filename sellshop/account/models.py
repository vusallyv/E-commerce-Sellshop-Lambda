from django.db import models
from django.db.models.expressions import F

# Create your models here.

class User(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=30, help_text="Max 30 char.", null=False, blank=False)
    last_name = models.CharField(verbose_name="Last Name", max_length=30, help_text="Max 30 char.", null=False, blank=False)
    email = models.EmailField(verbose_name="Email Address", null=False, blank=False, default="")
    birth = models.DateField(verbose_name="Date of Birth", null=True)
    country = models.CharField(verbose_name="Country", max_length=255, null=False, blank=False, default="")
    city = models.CharField(verbose_name="City", max_length=255, null=False, blank=False, default="")
    phone_number = models.IntegerField(verbose_name="Phone number", null=False, blank=False, default=0)
    additional_info = models.TextField(verbose_name="Additional Info", default="", null=True, blank=True)
    password = models.CharField(verbose_name="Password", max_length=30, null=False, blank=False, default="")

class Contact(models.Model):
    name = models.CharField(verbose_name="Name", max_length=30, help_text="Max 30 char.")
    email = models.EmailField(verbose_name="Email Address", null=False, blank=False, default="")
    message = models.TextField(verbose_name="Message")