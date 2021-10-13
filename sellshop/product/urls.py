from django.urls import path
from . import views

# app_name = 'product'

urlpatterns = [
    path('single-product/<int:pk>/', views.single_product, name="single_product"),
    path('product-list/', views.ProductListView.as_view(), name="product_list"),
]


