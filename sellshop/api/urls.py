from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register('users', views.UserViewSet)

auth_views = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('categories/', views.ListCategoryAPIView.as_view()),
    path('categories/<int:pk>/', views.DetailCategoryAPIView.as_view()),
    path('categories/create/', views.CreateCategoryAPIView.as_view()),
    path('categories/<int:pk>/update/', views.UpdateCategoryAPIView.as_view()),
    path('categories/<int:pk>/delete/', views.DeleteCategoryAPIView.as_view()),
    path('blogs/', views.BlogAPIView.as_view()),
    path('blogs/<int:pk>/', views.BlogAPIView.as_view()),
    path('comments/', views.CommentAPIView.as_view()),
    path('comments/<int:pk>/', views.CommentAPIView.as_view()),
    path('carts/', views.CartAPIView.as_view()),
    path('carts/<int:pk>/', views.CartAPIView.as_view()),
    path('blogs/create/', views.CreateBlogAPIView.as_view()),
    path('blogs/<int:pk>/update/', views.UpdateBlogAPIView.as_view()),
    path('blogs/<int:pk>/delete/', views.DeleteBlogAPIView.as_view()),
    path('products/', views.ProductAPIView.as_view(), name="products"),
    path('products/<int:pk>/', views.ProductAPIView.as_view(), name="product"),
    path('products/<int:product>/versions/',
         views.ProductVersionAPIVIew.as_view(), name="product_versions"),
    path('products/<int:product>/versions/<int:pk>/',
         views.ProductVersionAPIVIew.as_view(), name="product_version"),
    path('products/create/', views.ProductCreateAPIView.as_view(),
         name="product_create"),
    path('products/<int:pk>/destroy/',
         views.ProductDestroyAPIView.as_view(), name="product_destroy"),
    path('products/<int:pk>/update/',
         views.ProductUpdateAPIView.as_view(), name="product_update"),
    path('products/<int:product>/versions/create/',
         views.ProductVersionCreateAPIView.as_view(), name="product_version_create"),
    path('products/<int:product>/versions/<int:pk>/destroy/',
         views.ProductVersionDestroyAPIView.as_view(), name="product_version_destroy"),
    path('products/<int:product>/versions/<int:pk>/update/',
         views.ProductVersionUpdateAPIView.as_view(), name="product_version_update"),
    path('user/create/', views.UserCreateAPIView.as_view(), name="user"),
    path('', include(router.urls)),
    path('', include(auth_views)),
]
