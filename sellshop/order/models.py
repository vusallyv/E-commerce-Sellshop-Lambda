from django.db import models

# Create your models here.
from sellshop.utils.base_models import BaseModel
from django_countries.fields import CountryField


class Billing(BaseModel):
    user = models.OneToOneField(
        "user.User", related_name="User_Billing", on_delete=models.CASCADE, verbose_name="User")
    company_name = models.CharField(
        verbose_name="Company name", max_length=255, help_text="Max 255 char.", null=False, blank=False)
    country = CountryField(
        verbose_name="Country", max_length=255, null=False, blank=False)
    state = models.CharField(verbose_name="State",
                             max_length=255, null=False, blank=False)
    city = models.CharField(verbose_name="City",
                            max_length=255, null=False, blank=False)
    address = models.TextField(verbose_name="Address", null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.user}"


# class ShippingAddress(BaseModel):
#     user = models.ForeignKey(
#         "user.User", related_name="User_Shipping", on_delete=models.CASCADE, verbose_name="User")
#     first_name = models.CharField(
#         verbose_name="First name", max_length=30, help_text="Max 30 char.", null=False, blank=False)
#     last_name = models.CharField(
#         verbose_name="Last name", max_length=30, help_text="Max 30 char.", null=False, blank=False)
#     phone_number = models.CharField(
#         verbose_name="Phone number", max_length=30, help_text="Max 30 char.", null=False, blank=False)
#     company_name = models.CharField(
#         verbose_name="Company name", max_length=255, help_text="Max 255 char.", null=False, blank=False)
#     country = CountryField(
#         verbose_name="Country", max_length=255, null=False, blank=False)
#     state = models.CharField(verbose_name="State",
#                              max_length=255, null=False, blank=False)
#     city = models.CharField(verbose_name="City",
#                             max_length=255, null=False, blank=False)
#     address = models.TextField(verbose_name="Address", null=False, blank=False)

#     def __str__(self) -> str:
#         return f"{self.first_name} {self.last_name}"


class Wishlist(BaseModel):
    user = models.OneToOneField(
        "user.User", on_delete=models.CASCADE, default="")
    product = models.ManyToManyField(
        'product.ProductVersion', blank=True, related_name='Product_wishlist')

    def __str__(self):
        return f"{self.user}"


class Cart(BaseModel):
    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, default="")
    product = models.ManyToManyField(
        "product.ProductVersion", blank=True)
    is_ordered = models.BooleanField(verbose_name="Is Ordered?", default=False)

    def __str__(self) -> str:
        return f"{self.user}"


class Cart_Item(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(
        "product.ProductVersion", on_delete=models.CASCADE, blank=True)
    quantity = models.PositiveIntegerField("quantity", default=0)

    def __str__(self) -> str:
        return f"{self.cart}"
