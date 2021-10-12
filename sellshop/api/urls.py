from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ProductAPIView.as_view(), name="products"),
    path('products/<int:pk>/', views.ProductAPIView.as_view(), name="product"),
]