from django.urls import path
from django.views.decorators.http import require_POST
from . import views

# app_name = 'product'

urlpatterns = [
    path('single-product/<int:pk>/', views.single_product, name="single_product"),
    path('product-list/', views.product_list, name="product_list"),
]


