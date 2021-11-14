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
    if request.method == "POST":
        shipping = ShippingAddressForm(request.POST)
        if shipping.is_valid():
            shipping = ShippingAddress(
                user=request.user,
                company_name=request.POST.get('company_name'),
                country=Country.objects.get(id=request.POST.get('country')),
                city=City.objects.get(id=request.POST.get('city')),
                address=request.POST.get('address'),
            )

            shipping.save()
            Cart.objects.filter(is_ordered=False).filter(user=request.user).update(
                is_ordered=True, shipping_address=shipping)
            user_cart = Cart.objects.filter(user=request.user).filter(
                is_ordered=True).filter(shipping_address=shipping).first()
            for i in range(len(Cart_Item.objects.filter(cart=user_cart))):
                quantity = Cart_Item.objects.filter(cart=user_cart)[
                    i].product.quantity - Cart_Item.objects.filter(cart=user_cart)[i].quantity
                ProductVersion.objects.filter(id=Cart_Item.objects.filter(
                    cart=user_cart)[i].product.id).update(quantity=quantity)
    else:
        shipping = ShippingAddressForm()

    try:
        cart = len(Cart_Item.objects.filter(
            cart=Cart.objects.get(user=request.user, is_ordered=False)))
    except:
        cart = 0

    context = {
        'title': 'Checkout Sellshop',
        'shipping': shipping,
        'cart_products': cart,
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
    Wishlist.objects.get_or_create(user=request.user)
    qs_wishlist = Wishlist.objects.get(user=request.user).product.all()
    context = {
        'title': 'Wishlist Sellshop',
        'wishlist': qs_wishlist,
    }
    if request.user.is_authenticated:
        return render(request, "wishlist.html", context=context)
    return render(request, "error-404.html", context=context)



class SuccessView(TemplateView):
    template_name = 'success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


class CancelView(TemplateView):
    template_name = 'cancel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


class PaymentView(View):
    def post(self, request, *args, **kwargs):
        arr = []
        for i in range(len(Cart_Item.objects.filter(cart=Cart.objects.get(user=request.user, is_ordered=False)))):
            arr.append(Cart_Item.objects.filter(cart=Cart.objects.get(
                user=request.user, is_ordered=False))[i].product)
        print(arr)
        domain = 'http://127.0.0.1:8000/en/order'
        stripe.api_key = 'sk_test_51JvSjvJQqk33RMYtOTXJxE01aMel2Zd6TuCmshYksdWQuzUsl9oH05xCfOI9NhkX8c1aM7MBNfuiYqTjYGy2Rdw200LrGFS4Rv'
        line_items = []
        for i in range(len(arr)):
            line_items.append(
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(arr[i].product.price)*100,
                        'product_data': {
                            'name': arr[i].product.title,
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': Cart_Item.objects.filter(cart=Cart.objects.get(
                        user=request.user, is_ordered=False))[i].quantity,
                }
            )

        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            payment_method_types=[
                'card',
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url, code=303)
