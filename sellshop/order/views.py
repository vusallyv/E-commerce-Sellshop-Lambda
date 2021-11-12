from django.views.generic import View, TemplateView
from django.shortcuts import redirect, render

# Create your views here.
import stripe
from django.conf import settings
from django.http import JsonResponse

from order.forms import ShippingAddressForm
from order.models import Cart, Cart_Item, ShippingAddress, Wishlist
from product.models import ProductVersion


def card(request):
    context = {
        'title': 'Card Sellshop'
    }
    if request.user.is_authenticated:
        return render(request, "cart.html", context=context)
    return render(request, "error-404.html", context=context)


def checkout(request):
    # Cart.objects.get_or_create(user=request.user)
    if request.method == "POST":
        shipping = ShippingAddressForm(request.POST)
        if shipping.is_valid():
            shipping = ShippingAddress(
                user=request.user,
                company_name=request.POST.get('company_name'),
                country=request.POST.get('country'),
                state=request.POST.get('state'),
                city=request.POST.get('city'),
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
            return redirect('checkout')
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


class PaymentView(View):
    def post(self, request, *args, **kwargs):
        product = ProductVersion.objects.get(id=1)
        print(product)
        domain = 'http://127.0.0.1:8000/en/order'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(product.product.price)*1000,
                        'product_data': {
                            'name': product.product.title,
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            payment_method_types=[
                'card',
            ],
            mode='payment',
            success_url= domain + '/success/',
            cancel_url= domain + '/cancel/',
        )
        return JsonResponse({'id': checkout_session.id})

class ProductLandingPageView (TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STRIPE_SECRET_KEY'] = settings.STRIPE_SECRET_KEY
        # context['products'] = Cart_Item.objects.filter(cart=Cart.objects.get(user=self.request.user, is_ordered=False))
        context['products'] = ProductVersion.objects.get(id=1)
        return context

class SuccessView(TemplateView):
    template_name = 'success.html'

class CancelView(TemplateView):
    template_name = 'cancel.html'