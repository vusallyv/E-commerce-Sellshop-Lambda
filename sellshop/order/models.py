from django.db import models

# Create your models here.


class Billing(models.Model):
    user = models.ForeignKey(
        "user.User", related_name="User_Billing", on_delete=models.CASCADE, verbose_name="User")
    company_name = models.CharField(
        verbose_name="Company name", max_length=255, help_text="Max 255 char.", null=False, blank=False)
    country = models.CharField(
        verbose_name="Country", max_length=255, null=False, blank=False)
    state = models.CharField(verbose_name="State",
                             max_length=255, null=False, blank=False)
    city = models.CharField(verbose_name="City",
                            max_length=255, null=False, blank=False)
    address = models.TextField(verbose_name="Address", null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.user}"


class ShippingAddress(models.Model):
    user = models.ForeignKey(
        "user.User", related_name="User_Shipping", on_delete=models.CASCADE, verbose_name="User")
    first_name = models.CharField(
        verbose_name="First name", max_length=30, help_text="Max 30 char.", null=False, blank=False)
    last_name = models.CharField(
        verbose_name="Last name", max_length=30, help_text="Max 30 char.", null=False, blank=False)
    phone_number = models.CharField(
        verbose_name="Phone number", max_length=30, help_text="Max 30 char.", null=False, blank=False)
    company_name = models.CharField(
        verbose_name="Company name", max_length=255, help_text="Max 255 char.", null=False, blank=False)
    country = models.CharField(
        verbose_name="Country", max_length=255, null=False, blank=False)
    state = models.CharField(verbose_name="State",
                             max_length=255, null=False, blank=False)
    city = models.CharField(verbose_name="City",
                            max_length=255, null=False, blank=False)
    address = models.TextField(verbose_name="Address", null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Wishlist(models.Model):
    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, default="")
    product = models.ManyToManyField(
        'product.ProductVersion', blank=True, related_name='Product_wishlist')

    def __str__(self):
        return f"{self.user}"


class Cart(models.Model):
    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, default="")
    product = models.ManyToManyField(
        "product.ProductVersion", blank=True)

    def __str__(self) -> str:
        return f"{self.user}"
