from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from order.models import Billing, Cart, Cart_Item, City, Country, Coupon, ShippingAddress, Wishlist


@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'country',)
    list_filter = ('company_name',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_ordered',)
    list_editable = ('is_ordered',)

    fieldsets = (
        ('Cart information', {
         'fields': ('get_user_username', 'is_ordered', 'ordered_at')}),
        ('Shipping information', {'fields': (
            'get_shipping_company', 'get_shipping_country', 'get_shipping_city', 'get_shipping_address',)}),
        ('Product information', {
         'fields': ('get_product',)}),
        ('Coupon information', {
            'fields': ('get_coupon', 'get_coupon_discount')}),
    )
    readonly_fields = ('get_user_username', 'get_shipping_address',
                       'get_shipping_country', 'get_shipping_city', 'get_product', 'get_shipping_company', 'get_coupon', 'get_coupon_discount')

    def get_user_username(self, obj):
        return obj.user.username
    get_user_username.short_description = 'Username'

    def get_coupon(self, obj):
        return obj.coupon.code
    get_coupon.short_description = 'Coupon'

    def get_coupon_discount(self, obj):
        return f"{obj.coupon.discount}%"
    get_coupon_discount.short_description = 'Discount'

    def get_shipping_company(self, obj):
        return obj.shipping_address.company_name
    get_shipping_company.short_description = 'Shipping Company'

    def get_shipping_address(self, obj):
        return obj.shipping_address.address
    get_shipping_address.short_description = 'Shipping Address'

    def get_shipping_country(self, obj):
        return obj.shipping_address.city.country
    get_shipping_country.short_description = 'Shipping Country'

    def get_shipping_city(self, obj):
        return obj.shipping_address.city.city
    get_shipping_city.short_description = 'Shipping City'

    def get_product(self, obj):
        img = '''<table class="table">
                <thead class="thead-dark">
                    <tr>
                    <th scope="col">Title</th>
                    <th scope="col">Unit Price</th>
                    <th scope="col">Color</th>
                    <th scope="col">Size</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Total Price</th>
                    </tr>
                </thead>
                <tbody>
                '''
        for item in obj.User_Cart.all():
            img += f'''
            
                    <tr>
                        <td>{item.product.product.title}</td>
                        <td>{item.product.product.price}</td>
                        <td>{item.product.color.title}</td>
                        <td>{item.product.size.title}</td>
                        <td>{item.quantity}</td>
                        <td>{item.quantity*item.product.product.price}</td>
                    </tr>
                
            '''
        img += '</tbody></table>'
        if len(obj.User_Cart.all()) == 0:
            return 'No items in cart'
        return format_html(img)
    get_product.short_description = 'Products'


@admin.register(Cart_Item)
class Cart_ItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'get_cart_detail')
    list_editable = ('quantity',)

    def get_cart_detail(self, obj):
        return obj.cart.is_ordered
    get_cart_detail.short_description = 'Is Ordered?'


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'country',)
    list_filter = ('company_name', 'user', 'country')


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount',)
    list_filter = ('code', 'discount')


admin.site.register([Wishlist, Country, City])
