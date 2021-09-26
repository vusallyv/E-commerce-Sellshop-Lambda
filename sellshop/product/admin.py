from django.contrib import admin

# Register your models here.

from product.models import (
    Product, Category, Brand, ProductVersion, Subcategory, Review, Comment, Blog, Image
)


class ProductVersionAdmin(admin.ModelAdmin):
    search_fields = ['user_id']
    # autocomplete_fields = ['wishlist_id']


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductVersion,  ProductVersionAdmin)
admin.site.register(Subcategory)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Blog)
admin.site.register(Image)