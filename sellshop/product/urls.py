from django.urls import path, include
from django.urls.resolvers import URLPattern

from . import views


urlpatterns = [
    path('product-list/', views.product_list, name="product_list"),
    path('single-blog/<int:pk>/', views.single_blog, name="single_blog"),
    path('single-product/<int:pk>/', views.single_product, name="single_product"),
]
