from django.db import models
from django.contrib.auth.models import AbstractUser
from sellshop.utils.base_models import BaseModel


class Contact(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    email = models.EmailField(verbose_name="Email",
                              null=False, blank=False, default="")
    message = models.CharField(max_length=1000, verbose_name="Message")

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField(('email address'), blank=True, unique=True)
    birth = models.DateField(verbose_name="Date of Birth", null=True)
    country = models.CharField(
        verbose_name="Country", max_length=255, null=False, blank=False, default="")
    city = models.CharField(
        verbose_name="City", max_length=255, null=False, blank=False, default="")
    phone_number = models.IntegerField(
        verbose_name="Phone number", null=False, blank=False, default=0)
    additional_info = models.TextField(
        verbose_name="Additional Info", default="", null=True, blank=True)
    image = models.ImageField(
        verbose_name="User Image", upload_to="users/", default="staticfiles/img/blog/author1.png")
    rememberme = models.BooleanField(
        verbose_name="Remember me", default=False, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.username}"
