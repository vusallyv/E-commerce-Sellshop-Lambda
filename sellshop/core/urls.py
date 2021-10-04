from django.urls import path, include
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name="about"),
    path('error_404/', views.ErrorView.as_view(), name="error_404"),
    path('index/', views.HomeView.as_view(), name="index"),
]