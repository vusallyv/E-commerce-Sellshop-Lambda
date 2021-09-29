from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from product.models import (
    Product, Category, Brand, ProductVersion, Subcategory, Review, Comment, Blog, Image, Tag
)


class ProductVersionAdmin(admin.ModelAdmin):
    search_fields = ['user_id']
    
    def get_image(self,obj):
        if obj.image:
            img = '<img src="{}" width="100" height="100" />'.format(obj.image.url)
            return format_html(img)
        return 'No Image'
    
    # autocomplete_fields = ['wishlist_id']


admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductVersion,  ProductVersionAdmin)
admin.site.register(Subcategory)
admin.site.register(Review)
admin.site.register(Image)