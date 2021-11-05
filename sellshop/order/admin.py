from django.contrib import admin

# Register your models here.

from order.models import Billing, Cart, Cart_Item, Wishlist


# class Wishlistadmin(admin.ModelAdmin):
#     search_fields = ['user_id']


# admin.site.register(Billing)
# admin.site.register(Cart)
# admin.site.register(Wishlist)

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'country',)
    list_filter = ('company_name',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_ordered',)
    list_editable = ('is_ordered',)

@admin.register(Cart_Item)
class Cart_ItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity',)
    list_editable = ('quantity',)


# @admin.register(ShippingAddress)
# class ShippingAddressAdmin(admin.ModelAdmin):
#     list_display = ('user', 'phone_number', 'company_name', 'country',)
#     list_filter = ('company_name', 'user', 'country')


admin.site.register(Wishlist)
