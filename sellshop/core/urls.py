from django.urls import path, include

from . import views

urlpatterns = [
    path('about/', views.about, name="about"),
    # path('error_404/', views.ErrorView.as_view(), name="error_404"),
    path('set_language/', views.change_language, name="set_language")
]