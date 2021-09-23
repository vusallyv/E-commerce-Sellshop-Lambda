from django.urls import path, include
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('about/', views.about, name="about"),
    path('blog/', views.blog, name="blog"),
    path('error_404/', views.error_404, name="error_404"),
    path('index/', views.index, name="index"),
]