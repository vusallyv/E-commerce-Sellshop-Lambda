from django.db import models

# Create your models here.

class Billing(models.Model):
    user_id = models.ForeignKey("account.User", related_name="User_Billing", on_delete=models.CASCADE, default=1)
    company_name = models.CharField(verbose_name="Company name", max_length=255, help_text="Max 255 char.", null=False, blank=False)
    country = models.CharField(verbose_name="Country", max_length=255, null=False, blank=False)
    state = models.CharField(verbose_name="State", max_length=255, null=False, blank=False)
    city = models.CharField(verbose_name="City", max_length=255, null=False, blank=False)
    address = models.TextField(verbose_name="Address", null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.user_id.first_name} {self.user_id.last_name}"

class Wishlist(models.Model):
    user_id = models.ForeignKey("account.User", related_name="User_Wishlist", on_delete=models.CASCADE)
    products = models.ManyToManyField("product.ProductVersion", related_name="Wishlist_Product", blank=False)

    def __str__(self) -> str:
        return f"{self.user_id.first_name} {self.user_id.last_name}"

class Cart(models.Model):
    user_id = models.ForeignKey("account.User", related_name="User_Cart", on_delete=models.CASCADE)
    products = models.ManyToManyField("product.ProductVersion", related_name="Cart_Product", blank=False)

    def __str__(self) -> str:
        return f"{self.user_id.first_name} {self.user_id.last_name}"