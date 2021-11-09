from django.urls import path
from . import views

# app_name = 'product'

urlpatterns = [
    path('single-product/<int:pk>/', views.ProductDetailView.as_view(), name="single_product"),
    path('product-list/', views.PaginatorProductList, name="product_list"),

]


