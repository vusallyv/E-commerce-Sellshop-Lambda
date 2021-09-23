from django.contrib import admin

# Register your models here.

from product.models import Product, Category, Brand, ProductVersion, Subcategory, Review, Comment, Blog, Image

admin.site.register([Product, Category, Brand, ProductVersion, Subcategory, Review, Comment, Blog, Image])
