from django.urls import path, include
from . import views

urlpatterns = [
    path("cart/", views.card, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("order-complete/", views.order_complete, name="order_complete"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path('paypal-return/', views.PaypalReturnView.as_view(), name='paypal-return'),
    path('paypal-cancel/', views.PaypalCancelView.as_view(), name='paypal-cancel'),
]
