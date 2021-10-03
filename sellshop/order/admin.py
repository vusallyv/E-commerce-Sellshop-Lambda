from django.contrib import admin

# Register your models here.

from order.models import Billing, Cart, Wishlist, ShippingAddress

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('user_id','company_name', 'country',)
    list_filter = ('company_name',)

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('user_id','phone_number','company_name', 'country',)
    list_filter = ('company_name','user_id','country')



admin.site.register([Cart, Wishlist])