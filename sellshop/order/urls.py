from django.urls import path, include
from . import views

urlpatterns = [
    path("cart/", views.card, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("order-complete/", views.order_complete, name="order_complete"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("payment/", views.PaymentView.as_view(), name="payment"),
    path("landing/", views.ProductLandingPageView.as_view(), name="landing"),
    path("cancel/", views.CancelView, name="cancel"),
    path("success/", views.SuccessView, name="success"),
]
