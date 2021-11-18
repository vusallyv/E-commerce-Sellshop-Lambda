from django.db import models
from django.contrib.auth.models import AbstractUser
from sellshop.utils.base_models import BaseModel


class Contact(BaseModel):
    name = models.CharField(verbose_name="Name", max_length=50)
    email = models.EmailField(verbose_name="Email",
                              null=False, blank=False, default="")
    message = models.CharField(max_length=1000, verbose_name="Message")

    def __str__(self):
        return self.name


class User(AbstractUser):
    first_name = models.CharField(verbose_name='First Name', max_length=150, null=True, blank=True)
    last_name = models.CharField(verbose_name='Last Name', max_length=150, null=True, blank=True)
    email = models.EmailField(verbose_name="Email Address", blank=True, unique=True)
    birth = models.DateField(verbose_name="Date of Birth", null=True)
    country = models.CharField(
        verbose_name="Country", max_length=255, null=True, blank=True)
    city = models.CharField(
        verbose_name="City", max_length=255, null=True, blank=True)
    phone_number = models.IntegerField(
        verbose_name="Phone number", null=True, blank=True)
    additional_info = models.TextField(
        verbose_name="Additional Info", default="", null=True, blank=True)
    image = models.ImageField(
        verbose_name="User Image", upload_to="users/", default="staticfiles/img/blog/author1.png")

    def __str__(self) -> str:
        return f"{self.username}"

class Subscriber(BaseModel):
    email = models.EmailField(verbose_name="Email", unique=True)

    def __str__(self) -> str:
        return self.email