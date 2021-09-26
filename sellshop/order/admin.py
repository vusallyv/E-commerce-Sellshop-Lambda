from django.contrib import admin

# Register your models here.

from order.models import Billing, Cart, Wishlist


class Wishlistadmin(admin.ModelAdmin):
    search_fields = ['user_id']


admin.site.register(Billing)
admin.site.register(Cart)
admin.site.register(Wishlist)

