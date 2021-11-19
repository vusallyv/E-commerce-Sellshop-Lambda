from datetime import datetime
from django.db.models.expressions import F
from django.http.response import JsonResponse
from django.views.generic import View, TemplateView
from django.shortcuts import redirect, render

# Create your views here.
import stripe
import os
# from django.conf import settings

from order.forms import ShippingAddressForm
from order.models import Cart, Cart_Item, City, Country, ShippingAddress, Wishlist
from product.models import ProductVersion


def card(request):
    context = {
        'title': 'Card Sellshop'
    }
    if request.user.is_authenticated:
        return render(request, "cart.html", context=context)
    return render(request, "error-404.html", context=context)


def checkout(request):
    try:
        cart = Cart_Item.objects.filter(
            cart=Cart.objects.get(user=request.user, is_ordered=False))
        counter = 0
        for i in range(len(cart)):
            if cart[i].product.quantity > 0:
                counter += 1
    except:
        counter = 0
    if request.method == "POST":
        form = ShippingAddressForm(request.POST)
        if form.is_valid() and counter > 0:
            shipping = ShippingAddress(
                user=request.user,
                company_name=request.POST.get('company_name'),
                country=Country.objects.get(id=request.POST.get('country')),
                city=City.objects.get(id=request.POST.get('city')),
                address=request.POST.get('address'),
            )
            shipping.save()
            arr = []
            for i in range(len(Cart_Item.objects.filter(cart=Cart.objects.get(user=request.user, is_ordered=False)))):
                arr.append(Cart_Item.objects.filter(cart=Cart.objects.get(
                    user=request.user, is_ordered=False))[i].product)
            domain = 'http://127.0.0.1:8000/en/order'
            stripe.api_key = 'sk_test_51JvSjvJQqk33RMYtOTXJxE01aMel2Zd6TuCmshYksdWQuzUsl9oH05xCfOI9NhkX8c1aM7MBNfuiYqTjYGy2Rdw200LrGFS4Rv'
            line_items = []
            try:
                discount = Cart.objects.get(user=request.user, is_ordered=False).coupon.discount
                discount = int(discount)
            except:
                discount = int(0)   
            for i in range(len(arr)):
                line_items.append(
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': int(arr[i].product.price*100*(100 - discount)/100),
                            'product_data': {
                                'name': arr[i].product.title,
                                # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                            },
                        },
                        'quantity': Cart_Item.objects.filter(cart=Cart.objects.get(
                            user=request.user, is_ordered=False))[i].quantity,
                    }
                )
            line_items.append(
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 15*100,
                        'product_data': {
                            'name': 'Shipping and Handling',
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1
                }
            )
            checkout_session = stripe.checkout.Session.create(
                line_items=line_items,
                payment_method_types=[
                    'card',
                ],
                mode='payment',
                success_url=domain + '/success/',
                cancel_url=domain + '/checkout/',
            )
            Cart.objects.filter(is_ordered=False).filter(user=request.user).update(
                is_ordered=True, shipping_address=shipping, ordered_at=datetime.now())
            user_cart = Cart.objects.filter(user=request.user).filter(
                is_ordered=True).filter(shipping_address=shipping).first()
            for i in range(len(Cart_Item.objects.filter(cart=user_cart))):
                quantity = Cart_Item.objects.filter(cart=user_cart)[
                    i].product.quantity - Cart_Item.objects.filter(cart=user_cart)[i].quantity
                ProductVersion.objects.filter(id=Cart_Item.objects.filter(
                    cart=user_cart)[i].product.id).update(quantity=quantity)
            Cart.objects.get_or_create(user=request.user, is_ordered=False)
            return redirect(checkout_session.url, code=303)
    else:
        form = ShippingAddressForm()

    context = {
        'title': 'Checkout Sellshop',
        'shipping': form,
        'cart_products': counter,
    }
    if request.user.is_authenticated:
        return render(request, "checkout.html", context=context)
    return render(request, "error-404.html", context=context)


def order_complete(request):
    context = {
        'title': 'Order Complete Sellshop'
    }
    if request.user.is_authenticated:
        return render(request, "order-complete.html", context=context)
    return render(request, "error-404.html", context=context)


def wishlist(request):
    context = {
        'title': 'Wishlist Sellshop',
    }
    if request.user.is_authenticated:
        return render(request, "wishlist.html", context=context)
    return render(request, "error-404.html", context=context)


class SuccessView(TemplateView):
    template_name = 'success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
