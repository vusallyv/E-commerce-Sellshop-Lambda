from django.urls import path
from . import views

# app_name = 'product'

urlpatterns = [
    path('<int:pk>/', views.ProductDetailView.as_view(), name="single_product"),
    path('', views.PaginatorProductList, name="product_list"),
    path('search/', views.SearchView.as_view(), name="search"),

]


