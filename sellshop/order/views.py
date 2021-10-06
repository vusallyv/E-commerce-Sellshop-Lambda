from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from user.models import User
from order.forms import BillingForm, ShippingAddressForm
from order.models import Billing, ShippingAddress, Wishlist


def card(request):
    context = {
        'title': 'Card Sellshop'
    }
    if request.user.is_authenticated:
        return render(request, "cart.html", context=context)
    return render(request, "error-404.html", context=context)


def checkout(request):
    if request.method == "POST" and "billing" in request.POST:
        billing = BillingForm(request.POST)
        if billing.is_valid():
            billing = Billing(
                user_id=request.user,
                company_name=request.POST.get('company_name'),
                country=request.POST.get('country'),
                state=request.POST.get('state'),
                city=request.POST.get('city'),
                address=request.POST.get('address'),
            )
            billing.save()
    else:
        billing = BillingForm()

    if request.method == "POST" and "shipping" in request.POST:
        shipping = ShippingAddressForm(request.POST)
        if shipping.is_valid():
            shipping = ShippingAddress(
                user_id=request.user,
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                phone_number=request.POST.get('phone_number'),
                company_name=request.POST.get('company_name'),
                country=request.POST.get('country'),
                state=request.POST.get('state'),
                city=request.POST.get('city'),
                address=request.POST.get('address'),
            )
            shipping.save()
    else:
        shipping = ShippingAddressForm()

    context = {
        'title': 'Checkout Sellshop',
        'billing': billing,
        'shipping': shipping,
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
    qs_wishlist = Wishlist.objects.get(user_id=request.user).products.all()
    context = {
        'title': 'Wishlist Sellshop',
        'wishlist': qs_wishlist,
    }
    if request.user.is_authenticated:
        return render(request, "wishlist.html", context=context)
    return render(request, "error-404.html", context=context)
