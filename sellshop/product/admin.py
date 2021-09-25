from django.contrib import admin

# Register your models here.

from product.models import Product, Category, Brand, ProductVersion, Review, Comment, Blog, Image, Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['title']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'ex_price', 'price')
    list_editable = ('ex_price', 'price',)
    list_filter = ('rating',)

@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('get_author', 'quantity', 'color', 'size', 'is_main',)
    list_editable = ('quantity', 'is_main')
    list_filter = ('color', 'is_main', 'size')
    autocomplete_fields = ['tag_id']
     
    def get_author(self, obj):
        return obj.product_id.title
    get_author.short_description = 'Title'

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator',)
    list_filter = ('creator',)
    


admin.site.register([Category, Brand, Review, Comment, Image])
