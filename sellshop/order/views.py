from django.urls import reverse
from django.views.generic import FormView, TemplateView
from django.db.models import Q
from django.shortcuts import redirect, render

# Create your views here.
from paypal.standard.forms import PayPalPaymentsForm
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
    # if request.method == "POST":
    #     billing = BillingForm(request.POST)
    #     # if billing.is_valid():
    #     if Billing.objects.filter(user=request.user).exists():
    #         Billing.objects.filter(user=request.user).update(
    #             company_name=request.POST.get('company_name'),
    #             country=request.POST.get('country'),
    #             state=request.POST.get('state'),
    #             city=request.POST.get('city'),
    #             address=request.POST.get('address'),
    #         )
    #     else:
    #         billing = Billing(
    #             user=request.user,
    #             company_name=request.POST.get('company_name'),
    #             country=request.POST.get('country'),
    #             state=request.POST.get('state'),
    #             city=request.POST.get('city'),
    #             address=request.POST.get('address'),
    #         )
    #         billing.save()
    #         # Billing.objects.filter(user=request.user)
    # else:
    #     billing = BillingForm()

    # Cart.objects.get_or_create(user=request.user)
    if request.method == "POST":
        shipping = ShippingAddressForm(request.POST)
        # if shipping.is_valid():
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
        # 'billing': billing,
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


class PaypalFormView(FormView):
    template_name = 'paypal_form.html'
    form_class = PayPalPaymentsForm

    def get_initial(self):
        return {
            "business": 'your-paypal-business-address@example.com',
            "amount": 20,
            "currency_code": "EUR",
            "item_name": 'Example item',
            "invoice": 1234,
            "notify_url": self.request.build_absolute_uri(reverse('paypal-ipn')),
            "return_url": self.request.build_absolute_uri(reverse('paypal-return')),
            "cancel_return": self.request.build_absolute_uri(reverse('paypal-cancel')),
            "lc": 'EN',
            "no_shipping": '1',
        }


class PaypalReturnView(TemplateView):
    template_name = 'paypal_success.html'


class PaypalCancelView(TemplateView):
    template_name = 'paypal_cancel.html'
