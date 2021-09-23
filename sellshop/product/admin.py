from django.contrib import admin

# Register your models here.

from product.models import Product, Category, Brand, ProductVersion, Subcategory, Review, Comment, Blog, Image, Tag

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'ex_price', 'price')
    list_editable = ('ex_price', 'price',)
    list_filter = ('rating',)

class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('get_author', 'quantity', 'color', 'size', 'is_main',)
    list_editable = ('quantity', 'is_main')
    list_filter = ('color', 'is_main', 'size')
     
    def get_author(self, obj):
        return obj.product_id.title
    get_author.short_description = 'Title'

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator',)
    list_filter = ('creator',)
    


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVersion, ProductVersionAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register([Category, Brand, Subcategory, Review, Comment, Image, Tag])
