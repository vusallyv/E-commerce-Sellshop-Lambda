from django.db import models

# Create your models here.
from sellshop.utils.base_models import BaseModel
from django_countries.fields import CountryField


class Country(BaseModel):
    country = CountryField(
        verbose_name="Country", max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.country}"

    class Meta:
        verbose_name_plural = "Countries"


class City(BaseModel):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, verbose_name="Country", related_name="City_Country")
    city = models.CharField(verbose_name="City",
                            max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.city}"

    class Meta:
        verbose_name_plural = "Cities"


class Billing(BaseModel):
    user = models.OneToOneField(
        "user.User", related_name="User_Billing", on_delete=models.CASCADE, verbose_name="User")
    company_name = models.CharField(
        verbose_name="Company name", max_length=255, help_text="Max 255 char.", null=True, blank=True)
    country = models.ForeignKey(Country,
                                verbose_name="Country", on_delete=models.CASCADE, related_name="Billing_Country")
    city = models.ForeignKey(City, on_delete=models.CASCADE,
                             verbose_name="City", related_name="Billing_City")
    address = models.TextField(verbose_name="Address", null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.user}"


class ShippingAddress(BaseModel):
    user = models.ForeignKey(
        "user.User", related_name="User_Shipping", on_delete=models.CASCADE, verbose_name="User")
    company_name = models.CharField(
        verbose_name="Company name", max_length=255, help_text="Max 255 char.", null=True, blank=True)
    country = models.ForeignKey(Country,
                                verbose_name="Country", on_delete=models.CASCADE, related_name="Shipping_Country")
    city = models.ForeignKey(City, on_delete=models.CASCADE,
                             verbose_name="City", related_name="Shipping_City")
    address = models.TextField(verbose_name="Address", null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.user}"


class Wishlist(BaseModel):
    user = models.OneToOneField(
        "user.User", on_delete=models.CASCADE, default="")
    product = models.ManyToManyField(
        'product.ProductVersion', blank=True, related_name='Product_wishlist')

    def __str__(self):
        return f"{self.user}"

class Coupon(BaseModel):
    code = models.CharField(max_length=255, unique=True)
    discount = models.FloatField(default=0.00)

    def __str__(self):
        return f"{self.code}"

class Cart(BaseModel):
    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, default="")
    product = models.ManyToManyField(
        "product.ProductVersion", blank=True)
    is_ordered = models.BooleanField(verbose_name="Is Ordered?", default=False)
    ordered_at = models.DateTimeField(
        verbose_name="Ordered at", null=True, blank=True)
    shipping_address = models.OneToOneField(
        ShippingAddress, null=True, blank=True, verbose_name="Shipping Address", on_delete=models.CASCADE)
    coupon = models.ForeignKey(
        Coupon, null=True, blank=True, verbose_name="Coupon", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user}"


class Cart_Item(BaseModel):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="User_Cart")
    product = models.ForeignKey(
        "product.ProductVersion", on_delete=models.CASCADE, blank=True, null=True, related_name="Product_Cart")
    quantity = models.PositiveIntegerField("quantity", default=0)

    def __str__(self) -> str:
        return f"{self.cart}"
