from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from account.models import User
from order.forms import BillingForm


def card(request):
    context = {
        'title': 'Card Sellshop'
    }
    return render(request, "cart.html", context=context)


def checkout(request):
    qs_user = User.objects.first()
    if request.method == "POST":
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'title': 'Checkout Sellshop',
        'user': qs_user,
        'form': BillingForm,
    }
    return render(request, "checkout.html", context=context)


def order_complete(request):
    context = {
        'title': 'Order Complete Sellshop'
    }
    return render(request, "order-complete.html", context=context)


def wishlist(request):
    context = {
        'title': 'Wishlist Sellshop'
    }
    return render(request, "wishlist.html", context=context)
