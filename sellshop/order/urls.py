from django.urls import path, include
from . import views

urlpatterns = [
    path("cart/", views.card, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("order-complete/", views.order_complete, name="order_complete"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("success/", views.SuccessView.as_view(), name="success"),
]

