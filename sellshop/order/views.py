from django.shortcuts import render

# Create your views here.
from order.forms import BillingForm
from order.models import Billing, Cart, Cart_Item, Wishlist


def card(request):
    context = {
        'title': 'Card Sellshop'
    }
    if request.user.is_authenticated:
        return render(request, "cart.html", context=context)
    return render(request, "error-404.html", context=context)


def checkout(request):
    if request.method == "POST":
        billing = BillingForm(request.POST)
        # if billing.is_valid():
        if Billing.objects.filter(user=request.user).exists:
            Billing.objects.filter(user=request.user).update(
                company_name=request.POST.get('company_name'),
                country=request.POST.get('country'),
                state=request.POST.get('state'),
                city=request.POST.get('city'),
                address=request.POST.get('address'),
            )
        else:
            billing = Billing(
                user=request.user,
                company_name=request.POST.get('company_name'),
                country=request.POST.get('country'),
                state=request.POST.get('state'),
                city=request.POST.get('city'),
                address=request.POST.get('address'),
            )
            billing.save()
    else:
        billing = BillingForm()

    # if request.method == "POST" and "shipping" in request.POST:
    #     shipping = ShippingAddressForm(request.POST)
    #     if shipping.is_valid():
    #         shipping = ShippingAddress(
    #             user=request.user,
    #             first_name=request.POST.get('first_name'),
    #             last_name=request.POST.get('last_name'),
    #             phone_number=request.POST.get('phone_number'),
    #             company_name=request.POST.get('company_name'),
    #             country=request.POST.get('country'),
    #             state=request.POST.get('state'),
    #             city=request.POST.get('city'),
    #             address=request.POST.get('address'),
    #         )
    #         shipping.save()
    # else:
    #     shipping = ShippingAddressForm()

    context = {
        'title': 'Checkout Sellshop',
        'billing': billing,
        # 'shipping': shipping,
        'cart_products': Cart_Item.objects.filter(cart=Cart.objects.get(user=request.user)),
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
