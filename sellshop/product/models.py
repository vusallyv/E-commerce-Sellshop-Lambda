from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

from django.utils import timezone


class Brand(models.Model):
    title = models.CharField(verbose_name="Title",
                             max_length=30, help_text="Max 30 char.")

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    title = models.CharField(verbose_name="Title",
                             max_length=30, help_text="Max 30 char.")
    subcategory = models.ForeignKey('self', verbose_name="Subcategory", on_delete=models.CASCADE,
                                    null=True, blank=True, default="", related_name="subcategories")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField("Title", max_length=30, help_text="Max 30 char.")
    subtitle = models.CharField(
        "Subtitle", max_length=30, help_text="Max 30 char.")
    ex_price = models.DecimalField(
        verbose_name="Ex Price", max_digits=10, decimal_places=2)
    price = models.DecimalField(
        verbose_name="Price", max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name="Description")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.CASCADE, default="")

    def __str__(self) -> str:
        return self.title


class Color(models.Model):
    title = models.CharField(verbose_name="Title",
                             max_length=30, help_text="Max 30 char.")

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(verbose_name="Title",
                             max_length=30, help_text="Max 30 char.")

    def __str__(self):
        return self.title


class ProductVersion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default="")
    quantity = models.PositiveIntegerField(verbose_name='Quantity')
    color = models.ForeignKey(
        Color, default=1, verbose_name='Color', on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE,
                             default=1, verbose_name='Size')
    rating = models.DecimalField(
        verbose_name="Rating", max_digits=3, decimal_places=1, default=0)
    tag = models.ManyToManyField(
        "product.Tag", related_name="ProductVersion_Tags", null=True, blank=True)
    is_main = models.BooleanField(verbose_name='Main', default=False)

    def __str__(self):
        return self.product.title


class Tag(models.Model):
    title = models.CharField(verbose_name="Title",
                             max_length=255, help_text="Max 255 char.")

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    user = models.ForeignKey(
        "account.User", verbose_name="User", on_delete=models.CASCADE, default="")
    review = models.TextField(verbose_name="Review")
    rating = models.DecimalField(
        verbose_name="Rating", max_digits=2, decimal_places=1, default=0)
    created_at = models.DateTimeField(
        verbose_name="Created_at", default=timezone.now())
    product = models.ForeignKey(
        ProductVersion, on_delete=models.CASCADE, default="")

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}'s review"


class Image(models.Model):
    image = models.ImageField(verbose_name="Image",
                              upload_to="media/", null=True)
    productversion_id = models.ForeignKey(
        "product.ProductVersion", on_delete=models.CASCADE, verbose_name="Product Version")

    def __str__(self) -> str:
        return f"{self.image}"


class Blog(models.Model):
    title = models.CharField("Title", max_length=30, help_text="Max 30 char.")
    description = models.TextField(verbose_name="Description")
    creator = models.ForeignKey("account.User", on_delete=models.CASCADE)
    created_at = models.DateField(verbose_name="Created_at")
    like = models.PositiveIntegerField(verbose_name="Like")
    product = models.ForeignKey(
        ProductVersion, on_delete=models.CASCADE, default="")

    def __str__(self) -> str:
        return f"{self.title}"


class Comment(models.Model):
    user_id = models.ForeignKey(
        "account.User", verbose_name="User", on_delete=models.CASCADE, default="")
    description = models.TextField(verbose_name="Description")
    created_at = models.DateField(verbose_name="Created_at")
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, default=0, related_name="replies")

    def __str__(self) -> str:
        return f"{self.description}"
