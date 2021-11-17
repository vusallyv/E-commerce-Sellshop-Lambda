from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from product.models import Color, Product, Category, Brand, ProductVersion, Size, Review, Image, Tag

from django.utils.translation import gettext_lazy as _
# from django.contrib.flatpages.models import FlatPage

# from product.forms import FlatpageCustomForm


@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'color', 'size', 'is_main')
    list_editable = ('quantity','is_main')
    search_fields = ['product']

    # def get_image(self, obj):
    #     if obj.version_images:
    #         img = '<img src="{}" width="100" height="100" />'.format(
    #             obj.version_images)
    #         return format_html(img)
    #     return 'No Image'

    # autocomplete_fields = ['wishlist']


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


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('get_user_details', 'review', 'rating', )
    list_editable = ('rating',)

    def get_user_details(self, obj):
        return obj.user.username
    get_user_details.short_description = 'Username'


admin.site.register([Color, Category, Brand, Size])
# admin.site.unregister(FlatPage)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'productversion', 'is_main')
    list_editable = ('is_main',)

    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
    image_tag.short_description = 'Image'


# @admin.register(FlatPage)
# class FlatPageAdmin(admin.ModelAdmin):
#     form = FlatpageCustomForm
#     fieldsets = (
#         (None, {'fields': ('url', 'title', 'content', 'sites')}),
#         (_('Advanced options'), {
#             'classes': ('collapse',),
#             'fields': ('registration_required', 'template_name'),
#         }),
#     )
#     list_display = ('url', 'title')
#     list_filter = ('sites', 'registration_required')
#     search_fields = ('url', 'title')
