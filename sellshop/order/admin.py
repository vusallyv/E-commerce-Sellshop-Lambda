from django.contrib import admin

# Register your models here.

from order.models import Billing, Cart, Wishlist

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('user_id','company_name', 'country',)
    list_filter = ('company_name',)



admin.site.register([Cart, Wishlist])