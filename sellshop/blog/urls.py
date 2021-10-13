from django.urls import path

from . import views
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    path('', views.BlogListView.as_view(), name="blog"),
    path('single-blog/<int:pk>/', views.single_blog, name="single_blog"),
]
