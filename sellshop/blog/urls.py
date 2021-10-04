from django.urls import path, include
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.Bloglist.as_view(), name="blog"),
    path('single-blog/<int:pk>/', views.single_blog, name="single_blog"),
    # path('single-blog/<int:pk>/', views.single_blog, name="single_blog"),
]