from django.db import models

# Create your models here.

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
    category_id = models.ManyToManyField(Category, related_name="Product_Category")

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"
    
    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    title = models.CharField("Title", max_length=30, help_text="Max 30 char.")
    subtitle = models.CharField("Subtitle", max_length=30, help_text="Max 30 char.")
    ex_price = models.DecimalField(verbose_name="Ex Price", max_digits=10, decimal_places=2)
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name="Description")
    rating = models.DecimalField(verbose_name="Rating", max_digits=3, decimal_places=1)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag_id = models.ManyToManyField("product.Tag", related_name="Product_Tags")

    def __str__(self) -> str:
        return self.title

class ProductVersion(models.Model):
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
    quantity = models.IntegerField(verbose_name='Quantity')
    color = models.IntegerField(choices=colors, default=1, verbose_name='Color')
    size = models.IntegerField(choices=sizes, default=1, verbose_name='Size')
    wishlist_id = models.ManyToManyField("order.Wishlist", related_name="Wishlist_Product", blank=False)
    cart_id = models.ManyToManyField("order.Cart", related_name="Cart_Product", blank=False)
    is_main = models.BooleanField(verbose_name='Is_main', default=False)
        
    def __str__(self):
        return self.product_id.title

class Tag(models.Model):
    title = models.CharField("Title", max_length=255, help_text="Max 255 char.")

    def __str__(self) -> str:
        return self.title

class Review(models.Model):
    name = models.CharField(verbose_name="Name", max_length=30, help_text="Max 30 char.")
    email = models.CharField(verbose_name="Email", max_length=30, help_text="Max 30 char.")
    review = models.TextField(verbose_name="Review")
    rating = models.IntegerField(verbose_name="Rating")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Image(models.Model):
    image = models.ImageField(verbose_name="Image", upload_to="media/")
    product_id = models.ForeignKey("product.Product", on_delete=models.CASCADE, verbose_name="Product")

    def __str__(self) -> str:
        return f"{self.image}"

class Blog(models.Model):
    title = models.CharField("Title", max_length=30, help_text="Max 30 char.")
    description = models.TextField(verbose_name="Description")
    creator = models.ForeignKey("account.User", on_delete=models.CASCADE)
    created_at = models.DateField(verbose_name="Created_at")
    like = models.IntegerField(verbose_name="Like")
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"

class Comment(models.Model):
    description = models.IntegerField(verbose_name="Description")
    created_at = models.DateField(verbose_name="Created_at")
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_id = models.ForeignKey('product.Comment', on_delete=models.CASCADE)