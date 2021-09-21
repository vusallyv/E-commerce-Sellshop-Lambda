from django.contrib import admin

# Register your models here.

from product.models import Quantity, Product, Category, Brand, Color, Size, Subcategory, Quantity, Review, Comment, Self_Comment, Blog, Image

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Subcategory)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Self_Comment)
admin.site.register(Blog)
admin.site.register(Image)
admin.site.register(Quantity)