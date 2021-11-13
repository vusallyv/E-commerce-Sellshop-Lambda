from django.urls import path, include

from . import views

urlpatterns = [
    path('about/', views.about, name="about"),
    path('error_404/', views.ErrorView.as_view(), name="error_404"),
    path('index/', views.HomeView.as_view(), name="index"),
    path('base/', views.BaseView.as_view(), name="base"),
    path('set_language/', views.change_language, name="set_language")
]