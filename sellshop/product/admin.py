from django.contrib import admin

# Register your models here.

from product.models import Product, Product_Category, Product_Brand, Product_Color, Product_Size, Product_Subcategory

admin.site.register(Product)
admin.site.register(Product_Category)
admin.site.register(Product_Brand)
admin.site.register(Product_Color)
admin.site.register(Product_Size)
admin.site.register(Product_Subcategory)