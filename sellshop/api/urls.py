from django.urls import path, include
from rest_framework.generics import ListCreateAPIView
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [

    #  this def method
    # path('cartegory-get/', views.CategoriesList),
    # path('cartegory-get/<int:pk>/', views.CategoriesDetail),
    # path('cartegory-create/', views.CategoriesCreate),
    # path('cartegory-update/<int:pk>/', views.CategoriesUpdate),
    # path('cartegory-delete/<int:pk>/', views.CategoriesDelete),
    
    
    # this class method
    path('cartegory-list/', views.ListCategoryAPIView.as_view()),
    path('cartegory-list/<int:pk>/', views.DetailCategoryAPIView.as_view()),
    path('cartegory-create/', views.CreateCategoryAPIView.as_view()),
    path('cartegory-update/<int:pk>/', views.UpdateCategoryAPIView.as_view()),
    path('cartegory-delete/<int:pk>/', views.DeleteCategoryAPIView.as_view()),
    
    path('', include(router.urls)),
]