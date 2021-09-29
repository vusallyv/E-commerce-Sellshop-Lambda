from django.db import models
from django.db.models.fields.related import ForeignKey

from sellshop.utils.base_models import BaseModel
from blog.models import Comment, Blog

class Brand(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30, help_text="Max 30 char.")
    
    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30, help_text="Max 30 char.")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self) -> str:
        return self.title


class Subcategory(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30, help_text="Max 30 char.")
    category_id = models.ManyToManyField(Category, related_name="ProductCategory")

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"


class Product(models.Model):
    title = models.CharField("Title", max_length=30, help_text="Max 30 char.")
    subtitle = models.CharField("Subtitle", max_length=30, help_text="Max 30 char.")
    ex_price = models.DecimalField(verbose_name="Ex Price", max_digits=10, decimal_places=2)
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name="Description")
    rating = models.IntegerField(verbose_name="Rating")
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
   

    def __str__(self) -> str:
        return self.title
    


class Tag(models.Model):
    title = models.CharField(max_length=30, verbose_name='Title', help_text='Max 30 char.', unique=True)
    
    def __str__(self):
        return self.title
   
    
class ProductVersion(BaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    colors = (
        (1, 'Red'),
        (2, 'Blue'),
        (3, 'Black'),
        (4, 'Green'),
        (5, 'Yellow'),
        (6, 'White')
    )
    sizes = (
        (1, 'S'),
        (2, 'M'),
        (3, 'L'),
        (4, 'X'),
        (5, 'XL'),
        (6, 'XXL'),
        (7, '2XL'),
        (8, '3XL')
    )
    quantity = models.PositiveIntegerField(verbose_name='Quantity')
    color = models.IntegerField(choices=colors, default=1, verbose_name='Color')
    size = models.IntegerField(choices=sizes, default=1, verbose_name='Size')
    is_main = models.BooleanField(verbose_name='Is_main')
    tags = models.ManyToManyField("product.Tag", related_name="products")

        
    def __str__(self):
        return self.product_id.title


class Review(models.Model):
    name = models.CharField(verbose_name="Name", max_length=30, help_text="Max 30 char.")
    email = models.CharField(verbose_name="Email", max_length=30, help_text="Max 30 char.")
    review = models.CharField(max_length=300,verbose_name="Review")
    rating = models.IntegerField(verbose_name="Rating", default=0)
    product_id = models.ForeignKey(Product,null=True, blank=True,default="", on_delete=models.CASCADE) # bu commentde qalmasin
    
    def __str__(self):
        return self.review
    

class Image(models.Model):
    image = models.ImageField(verbose_name="Image", upload_to='products/images')
    product_id = models.ForeignKey(ProductVersion, on_delete=models.CASCADE, verbose_name="Prodcut_ID")


