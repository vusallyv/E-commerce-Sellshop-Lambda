from django.contrib import admin

# Register your models here.

from order.models import Billing, Cart, Wishlist

admin.site.register([Billing, Cart, Wishlist])