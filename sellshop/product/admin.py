from django.contrib import admin

# Register your models here.

from product.models import Color, Product, Category, Brand, ProductVersion, Review, Comment, Blog, Image, Size, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'ex_price', 'price', 'get_brand')
    list_editable = ('ex_price', 'price',)

    def get_brand(self, obj):
        return obj.brand.title
    get_brand.short_description = 'Brand'


@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'quantity', 'color', 'size', 'is_main',)
    list_editable = ('quantity', 'is_main')
    list_filter = ('color', 'is_main', 'size', 'rating')
    autocomplete_fields = ['tag']

    def get_title(self, obj):
        return obj.product.title
    get_title.short_description = 'Title'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator',)
    list_filter = ('creator',)


admin.site.register([Category, Brand, Review, Comment, Image, Color, Size])
