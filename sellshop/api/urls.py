from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ListProductAPIView.as_view(), name="products"),
    path('products/<int:pk>/', views.ProductAPIView.as_view(), name="product"),
    path('products/create/', views.ProductCreateAPIView.as_view(), name="product"),
    path('products/destroy/<int:pk>/', views.ProductDestroyAPIView.as_view(), name="product"),
    path('products/update/<int:pk>/', views.ProductUpdateAPIView.as_view(), name="product"),
    path('user/create/', views.UserCreateAPIView.as_view(), name="user"),
]
