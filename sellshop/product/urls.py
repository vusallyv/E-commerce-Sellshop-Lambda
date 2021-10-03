from django.urls import path
from django.views.decorators.http import require_POST
from . import views

# app_name = 'product'

urlpatterns = [
    path('product-list/', views.ProductListView.as_view(), name="product_list"),
    path('single-blog/<int:pk>/', views.single_blog, name="single_blog"),
    path('single-product/<int:pk>/', views.single_product, name="single_product"),
]


