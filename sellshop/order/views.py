from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def card(request):
    context = {
        'title': 'Card Sellshop'
    }
    return render(request, "cart.html", context=context)

def checkout(request):
    context = {
        'title': 'Checkout Sellshop'
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