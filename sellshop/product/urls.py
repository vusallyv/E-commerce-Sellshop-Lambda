from django.urls import path

from . import views

# app_name = 'product'

urlpatterns = [
    path('product-list/', views.ProductListView.as_view(), name="product_list"),
    path('single-blog/<int:pk>/', views.BlogDetailView.as_view(), name="single_blog"),
    path('single-product/<int:pk>/', views.ProductDetailView.as_view(), name="single_product"),
]
