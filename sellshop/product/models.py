from django.db import models
from sellshop.utils.base_models import BaseModel
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils import timezone

# from ckeditor_uploader.fields import RichTextUploadingField #niye gormur ???

User = get_user_model()


class Brand(BaseModel):
    title = models.CharField(verbose_name="Title",
                             max_length=30, help_text="Max 30 char.")

    def __str__(self) -> str:
        return self.title


class Category(BaseModel):
    title = models.CharField(verbose_name="Title",
                             max_length=30, help_text="Max 30 char.")
    parent = models.ForeignKey('self', verbose_name="Parent", on_delete=models.CASCADE,
                               null=True, blank=True, default="", related_name="parent_category")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title


class Product(BaseModel):
    title = models.CharField("Title", max_length=30, help_text="Max 30 char.")
    subtitle = models.CharField(
        "Subtitle", max_length=30, help_text="Max 30 char.")
    ex_price = models.DecimalField(
        verbose_name="Ex Price", max_digits=10, decimal_places=2)
    price = models.DecimalField(
        verbose_name="Price", max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name="Description")
    # description = RichTextUploaderField(null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    @property
    def main_version(self):
        return self.versions.filter(is_main=True).first()


class Tag(BaseModel):
    title = models.CharField(
        max_length=30, verbose_name='Title', help_text='Max 30 char.', unique=True)

    def __str__(self):
        return self.title


class Color(BaseModel):
    title = models.CharField(verbose_name="Title",
                             max_length=30, help_text="Max 30 char.")

    def __str__(self):
        return self.title


class Size(BaseModel):
    title = models.CharField(verbose_name="Title",
                             max_length=30, help_text="Max 30 char.")

    def __str__(self):
        return self.title


class Product(BaseModel):
    title = models.CharField("Title", max_length=30, help_text="Max 30 char.")
    subtitle = models.CharField(
        "Subtitle", max_length=30, help_text="Max 30 char.")
    ex_price = models.DecimalField(
        verbose_name="Ex Price", max_digits=10, decimal_places=2)
    price = models.DecimalField(
        verbose_name="Price", max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name="Description")
    # description = RichTextUploaderField(null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    @property
    def main_version(self):
        return self.versions.filter(is_main=True).first()

    @property
    def total_quantity(self):
        return sum([version.quantity for version in self.versions.all()])


class ProductVersion(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, default="", related_name="versions")
    quantity = models.PositiveIntegerField(verbose_name='Quantity', default=0)
    color = models.ForeignKey(
        Color, default=1, verbose_name='Color', on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE,
                             default=1, verbose_name='Size')
    rating = models.DecimalField(
        verbose_name="Rating", max_digits=3, decimal_places=1, default=0)
    tag = models.ManyToManyField(
        "product.Tag")
    is_main = models.BooleanField(verbose_name='Main', default=False)

    def __str__(self):
        return self.product.title


class Review(BaseModel):
    user = models.ForeignKey(
        "user.User", verbose_name="User", on_delete=models.CASCADE, default="")
    review = models.TextField(verbose_name="Review")
    rating = models.DecimalField(
        verbose_name="Rating", max_digits=2, decimal_places=1, default=0)
    product = models.ForeignKey(
        ProductVersion, on_delete=models.CASCADE, default="")

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"


class Image(BaseModel):
    image = models.ImageField(verbose_name="Image",
                              upload_to="media/", null=True)
    productversion = models.ForeignKey(
        ProductVersion, on_delete=models.CASCADE, verbose_name="Product Version")
    is_main = models.BooleanField(verbose_name="Is main?", default=False)

    def __str__(self) -> str:
        return f"{self.image}"
