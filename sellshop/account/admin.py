from django.contrib import admin

from account.models import Blog, Brand, Category, Comment, Image, Product, Product_version, Review, Subcategory


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(Product_version)
admin.site.register(Review)
admin.site.register(Image)
admin.site.register(Blog)
admin.site.register(Comment)