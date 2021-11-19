"""sellshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from core.views import index

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('rosetta/', include("rosetta.urls")),
    path("core/", include("core.urls")),
    path('', index, name="index"),
    path("product/", include("product.urls")),
    path("user/", include("user.urls")),
    path('user/', include('django.contrib.auth.urls')),
    path("order/", include("order.urls")),
    path("blog/", include("blog.urls")),
    path('api/', include('api.urls')),
    # path('jet/', include('jet.urls', 'jet')),
    # path('', include('django.contrib.flatpages.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
