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

class Product_version(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    colors = (
        (1, 'red'),
        (2, 'blue'),
        (3, 'red'),
        (4, 'black'),
        (5, 'green'),
        (6, 'yellow'),
        (7, 'white')
    )
    sizes = (
        (1, 'S'),
        (2, 'M'),
        (3, 'L'),
        (4, 'X'),
        (5, 'XL'),
        (6, 'XXl'),
        (7, '2XXl'),
        (8, '3XXl')
    )
    quantity = models.IntegerField(verbose_name='Quantity')
    color = models.IntegerField(choices=colors, default=1, verbose_name='Color')
    size = models.IntegerField(choices=sizes, default=1, verbose_name='Size')
    is_main = models.BooleanField(verbose_name='Is_main')
        
    # def __str__(self):
    #     return f'{self.product_id.title} version'

# class Color(models.Model):
#     color = models.CharField(verbose_name="Color", max_length=30, help_text="Max 30 char.")
#     product_id = models.ManyToManyField(Product, related_name="Product_Color")
    
# class Size(models.Model):
#     size = models.CharField(verbose_name="Size", max_length=30, help_text="Max 30 char.")
#     product_id = models.ManyToManyField(Product, related_name="Product_Size")
    
# class Quantity(models.Model):
#     quantity = models.CharField(verbose_name="Quantity", max_length=30, help_text="Max 30 char.")
#     product_id = models.ManyToManyField(Product, related_name="Product_Quantity")
    
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