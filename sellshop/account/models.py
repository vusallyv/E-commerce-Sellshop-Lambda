from django.db import models


from sellshop.utils.base_models import BaseModel


# class PracticModel(BaseModel):
#     REQUIRED_EXPERIENCE = (
#         (0, 'No experience required'),
#         (1, '1 year'),
#         (2, '2 year'),
#         (3, '3+ year'),
#     )
#     title = models.CharField(max_length=255,verbose_name='title',help_text='Max limit: 255 char.' )
#     description = models.TextField(verbose_name='Desc')
#     company = models.CharField(max_length=255,verbose_name='company', help_text='Max limit: 255 char.')
#     location = models.CharField(max_length=255,verbose_name='location', help_text='Max limit: 255 char.')
#     email = models.EmailField(verbose_name='email')
#     is_remote = models.BooleanField(default=True, verbose_name='Is remote friendly?')
#     salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salary')
#     required_experience = models.IntegerField(choices=REQUIRED_EXPERIENCE, default=0, verbose_name='Required experience')


#     class Meta:
#         verbose_name = "Practic post"
#         verbose_name_plural = "Practic posts"
        
#     def __str__(self):
#         return self.title












# class User(models.Model):
#     first_name = models.CharField(max_length=255,verbose_name='first_name',help_text='Max limit: 255 char.' )
#     last_name = models.CharField(max_length=255,verbose_name='last_name',help_text='Max limit: 255 char.' )
#     email = models.EmailField(verbose_name='email')
#     birth = models.DateTimeField(auto_now=True)
#     country = models.CharField(max_length=255,verbose_name='country', help_text='Max limit: 255 char.')
#     city = models.CharField(max_length=255,verbose_name='city', help_text='Max limit: 255 char.')
#     phone_number = models.CharField(max_length=255,verbose_name='phone_number')
#     add_info = models.TextField(verbose_name='Add_info')
#     password = models.CharField(max_length=255,verbose_name='password')
    

#     class Meta:
#         verbose_name = "User post"
#         verbose_name_plural = "User "
        
#     def __str__(self):
#         return self.first_name


# class Product(BaseModel):
#     img = models.ImageField(verbose_name='image')
#     title = models.CharField(max_length=255,verbose_name='title' )
#     fashion = models.CharField(max_length=255,verbose_name='fashion')
#     price = models.IntegerField(verbose_name='price')
#     last_price = models.IntegerField(verbose_name='laste_price')
#     rating = models.IntegerField(verbose_name='rating')
#     desc = models.CharField(max_length=255,verbose_name='desc')
#     tag_id = models.ForeignKey('account.Tag', on_delete=models.CASCADE)
#     subtitle = models.CharField(max_length=255,verbose_name='subtitle')
#     description = models.TextField(verbose_name='description')
#     rating = models.FloatField(verbose_name='rating')
    
    
    
#     class Meta:
#         verbose_name = "Product post"
#         verbose_name_plural = "Product "
        
#     def __str__(self):
#         return self.title



# class Product_version(models.Model):
#     product_id = models.ForeignKey('account.Product', on_delete=models.CASCADE)
#     color = (
#         (1, 'red'),
#         (2, 'blue'),
#         (3, 'red'),
#         (4, 'black'),
#         (5, 'green'),
#         (6, 'yellow'),
#         (7, 'white')
#     )
#     size = (
#         (1, 'S'),
#         (2, 'M'),
#         (3, 'L'),
#         (4, 'X'),
#         (5, 'XL'),
#         (6, 'XXl'),
#         (7, '2XXl'),
#         (8, '3XXl')
#     )
#     quantity = models.IntegerField(verbose_name='quantity')
#     color = models.IntegerField(choices=color, default=1, verbose_name='color')
#     size = models.IntegerField(choices=size, default=1, verbose_name='size')
#     is_main = models.BooleanField(verbose_name='is_main')
    
    
#     class Meta:
#         verbose_name = "Product version post"
#         verbose_name_plural = "Product version"
        
#     def __str__(self):
#         return f'{self.product_id.title} version'


    
# class Tag(models.Model):
#     fashion = models.CharField(max_length=255, verbose_name='fashion')
#     feature_products = models.IntegerField(verbose_name='feature_products')
#     feature_product = models.IntegerField(verbose_name='feature_product')
#     new_arr_popul_best = models.IntegerField(verbose_name='new_arr__popul__best')
#     latest_blog = models.CharField(max_length=255, verbose_name='latest_blog')

    
    
#     class Meta:
#         verbose_name = "Tag post"
#         verbose_name_plural = "Tag "
        
#     def __str__(self):
#         return self.fashion


# class Comment(models.Model):
#     autor = models.CharField(max_length=255, verbose_name='autor')
#     create_at = models.DateTimeField(auto_now_add=True)
#     parent_comment = models.ForeignKey('account.Comment', on_delete=models.CASCADE)
#     product_id = models.ForeignKey('account.Product', on_delete=models.CASCADE)
    
    
#     class Meta:
#         verbose_name = "Comment post"
#         verbose_name_plural = "Comment "
        
#     def __str__(self):
#         return self.autor
    
# ****************************************************************************************

# from django.db import models



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

    def __str__(self) -> str:
        return self.title

class Product_version(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    colors = (
        (1, 'red'),
        (2, 'blue'),
        (3, 'black'),
        (4, 'green'),
        (5, 'yellow'),
        (6, 'white'),
        (7, 'mix'),
    )
    sizes = (
        (1, 'S'),
        (2, 'M'),
        (3, 'L'),
        (4, 'X'),
        (5, 'XL'),
        (6, 'XXl'),
        (7, 'XXXl'),
    )
    quantity = models.IntegerField(verbose_name='Quantity')
    color = models.IntegerField(choices=colors, default=1, verbose_name='Color')
    size = models.IntegerField(choices=sizes, default=1, verbose_name='Size')
    is_main = models.BooleanField(verbose_name='Is_main')
        
    def __str__(self):
        return self.product_id.title

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

class Comment(BaseModel):
    description = models.IntegerField(verbose_name="Description")
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_id = models.ForeignKey('account.Comment', on_delete=models.CASCADE)