from django.urls import path

from . import views
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    path('', views.BlogList, name="blog"),
    path('<slug:slug>/', views.BlogDetailView.as_view(), name="single_blog"),
]
