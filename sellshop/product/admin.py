from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from product.models import Color, Product, Category, Brand, ProductVersion, Size, Review, Image, Tag


# @admin.register(ProductVersion)
# class ProductVersionAdmin(admin.ModelAdmin):
#     search_fields = ['user_id']

#     def get_image(self, obj):
#         if obj.image:
#             img = '<img src="{}" width="100" height="100" />'.format(
#                 obj.image.url)
#             return format_html(img)
#         return 'No Image'

#     # autocomplete_fields = ['wishlist_id']


# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     search_fields = ['title']


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'ex_price', 'price', 'get_brand')
#     list_editable = ('ex_price', 'price',)

#     def get_brand(self, obj):
#         return obj.brand.title
#     get_brand.short_description = 'Brand'


# @admin.register(ProductVersion)
# class ProductVersionAdmin(admin.ModelAdmin):
#     list_display = ('get_title', 'quantity', 'color', 'size', 'is_main',)
#     list_editable = ('quantity', 'is_main')
#     list_filter = ('color', 'is_main', 'size', 'rating')
#     autocomplete_fields = ['tag']

#     def get_title(self, obj):
#         return obj.product.title
#     get_title.short_description = 'Title'



admin.site.register([Color, Product, Category, Brand, ProductVersion, Size, Review, Image, Tag])
