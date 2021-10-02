from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from account.models import User
from order.forms import BillingForm


def card(request):
    context = {
        'title': 'Card Sellshop'
    }
    if request.user.is_authenticated:
        return render(request, "cart.html", context=context)
    return render(request, "error-404.html", context=context)


def checkout(request):
    if request.method == "POST":
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'title': 'Checkout Sellshop',
        'form': BillingForm,
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
        'title': 'Wishlist Sellshop'
    }
    if request.user.is_authenticated:
        return render(request, "wishlist.html", context=context)
    return render(request, "error-404.html", context=context)
