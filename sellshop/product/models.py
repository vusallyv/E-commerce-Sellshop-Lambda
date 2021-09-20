from django.db import models

# Create your models here.

class Product_Brand(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30, help_text="Max 30 char.")

class Product_Category(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30, help_text="Max 30 char.")

class Product_Subcategory(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30, help_text="Max 30 char.")
    category_id = models.ForeignKey(Product_Category, on_delete=models.CASCADE)

class Product(models.Model):
    title = models.CharField("Title", max_length=30, help_text="Max 30 char.")
    subtitle = models.CharField("Subtitle", max_length=30, help_text="Max 30 char.")
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name="Description")
    rating = models.DecimalField(verbose_name="Rating", max_digits=3, decimal_places=1)
    brand_id = models.ForeignKey(Product_Brand, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Product_Category, on_delete=models.CASCADE)

class Product_Size(models.Model):
    size = models.CharField(verbose_name="Size", max_length=30, help_text="Max 30 char.")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    
class Product_Color(models.Model):
    Color = models.CharField(verbose_name="color", max_length=30, help_text="Max 30 char.")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
