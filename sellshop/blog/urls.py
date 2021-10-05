from django.urls import path

from . import views

urlpatterns = [
    path('', views.Bloglist.as_view(), name="blog"),
    path('single-blog/<int:pk>/', views.SingleBlog.as_view(), name="single_blog"),
]
