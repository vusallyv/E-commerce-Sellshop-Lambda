from django.db import models

# Create your models here.

class Brand(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30, help_text="Max 30 char.")

class Category(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30, help_text="Max 30 char.")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Subcategory(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30, help_text="Max 30 char.")
    category_id = models.ManyToManyField(Category, related_name="Product_Category")

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"

class Product(models.Model):
    title = models.CharField("Title", max_length=30, help_text="Max 30 char.")
    subtitle = models.CharField("Subtitle", max_length=30, help_text="Max 30 char.")
    ex_price = models.DecimalField(verbose_name="Ex Price", max_digits=10, decimal_places=2)
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name="Description")
    rating = models.DecimalField(verbose_name="Rating", max_digits=3, decimal_places=1)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

class Color(models.Model):
    color = models.CharField(verbose_name="color", max_length=30, help_text="Max 30 char.")
    product_id = models.ManyToManyField(Product, related_name="Product_Color")
    
class Size(models.Model):
    size = models.CharField(verbose_name="Size", max_length=30, help_text="Max 30 char.")
    color_id = models.ManyToManyField(Color, related_name="Color_Size")
    
class Quantity(models.Model):
    quantity = models.CharField(verbose_name="quantity", max_length=30, help_text="Max 30 char.")
    size_id = models.ManyToManyField(Size, related_name="Size_Quantity")
    
class Review(models.Model):
    name = models.CharField(verbose_name="Name", max_length=30, help_text="Max 30 char.")
    email = models.CharField(verbose_name="Email", max_length=30, help_text="Max 30 char.")
    review = models.TextField(verbose_name="Review")
    rating = models.IntegerField(verbose_name="Rating")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Image(models.Model):
    image = models.CharField(verbose_name="Image", max_length=255, help_text="Max 255 char.")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Blog(models.Model):
    title = models.CharField("Title", max_length=30, help_text="Max 30 char.")
    description = models.TextField(verbose_name="Description")
    creator = models.CharField("Creator", max_length=30, help_text="Max 30 char.")
    created_at = models.DateField(verbose_name="Created_at")
    like = models.IntegerField(verbose_name="Like")
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    description = models.IntegerField(verbose_name="Description")
    created_at = models.DateField(verbose_name="Created_at")
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)

class Self_Comment(models.Model):
    description = models.IntegerField(verbose_name="Description")
    created_at = models.DateTimeField(verbose_name="Created_at")
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    

