from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ProductAPIView.as_view(), name="products"),
    path('products/<int:pk>/', views.ProductAPIView.as_view(), name="product"),
    path('products/<int:product>/versions/', views.ProductVersionAPIVIew.as_view(), name="product_versions"),
    path('products/<int:product>/versions/<int:pk>/', views.ProductVersionAPIVIew.as_view(), name="product_version"),
    path('products/create/', views.ProductCreateAPIView.as_view(), name="product_create"),
    path('products/<int:pk>/destroy/', views.ProductDestroyAPIView.as_view(), name="product_destroy"),
    path('products/<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name="product_update"),
    path('products/<int:product>/versions/create/', views.ProductVersionCreateAPIView.as_view(), name="product_version_create"),
    path('products/<int:product>/versions/<int:pk>/destroy/', views.ProductVersionDestroyAPIView.as_view(), name="product_version_destroy"),
    path('products/<int:product>/versions/<int:pk>/update/', views.ProductVersionUpdateAPIView.as_view(), name="product_version_update"),
    path('user/create/', views.UserCreateAPIView.as_view(), name="user"),
]
