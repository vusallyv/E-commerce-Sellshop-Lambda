from django.urls import path, include
from rest_framework.generics import ListCreateAPIView
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

    #  this category def method
    # path('cartegory-get/', views.CategoriesList),
    # path('cartegory-get/<int:pk>/', views.CategoriesDetail),
    # path('cartegory-create/', views.CategoriesCreate),
    # path('cartegory-update/<int:pk>/', views.CategoriesUpdate),
    # path('cartegory-delete/<int:pk>/', views.CategoriesDelete),
    
    # this category class method
    path('cartegory-list/', views.ListCategoryAPIView.as_view()),
    path('cartegory-list/<int:pk>/', views.DetailCategoryAPIView.as_view()),
    path('cartegory-create/', views.CreateCategoryAPIView.as_view()),
    path('cartegory-update/<int:pk>/', views.UpdateCategoryAPIView.as_view()),
    path('cartegory-delete/<int:pk>/', views.DeleteCategoryAPIView.as_view()),
    
    # this blog class method
    path('blog-list/', views.ListBlogAPIView.as_view()),
    path('blog-list/<int:pk>/', views.DetailListBlogAPIView.as_view()),
    path('blog-create/', views.CreateBlogAPIView.as_view()),
    path('blog-update/<int:pk>/', views.UpdateBlogAPIView.as_view()),
    path('blog-delete/<int:pk>/', views.DeleteBlogAPIView.as_view()),
    
    # include routes
    path('', include(router.urls)),
    
    # include auth_views
    path('', include(auth_views)),
    
]




    
