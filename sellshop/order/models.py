from django.db import models

# Create your models here.

class Billing(models.Model):
    name = models.CharField(verbose_name="Name", max_length=30, help_text="Max 30 char.", null=False, blank=False, default=0)
    phone_number = models.IntegerField(verbose_name="Phone number", null=False, blank=False, default=0)
    company_name = models.CharField(verbose_name="Email Address", max_length=255, help_text="Max 255 char.", null=False, blank=False)
    country = models.CharField(verbose_name="Country", max_length=255, null=False, blank=False)
    state = models.CharField(verbose_name="State", max_length=255, null=False, blank=False)
    city = models.CharField(verbose_name="City", max_length=255, null=False, blank=False)
    address = models.TextField(verbose_name="Address", null=False, blank=False)

class Wishlist(models.Model):
    user_id = models.ManyToManyField("account.User", related_name="User_Wishlist")

class Cart(models.Model):
    user_id = models.ManyToManyField("account.User", related_name="User_Cart")