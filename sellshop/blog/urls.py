from django.urls import path

from . import views
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    # path('', views.BlogListView.as_view(), name="blog"),
    path('', views.BlogList, name="blog"),
    path('<int:pk>/', views.BlogDetailView.as_view(), name="single_blog"),
]
