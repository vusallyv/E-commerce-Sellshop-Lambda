from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("contact/", views.ContactView.as_view(),
         name="contact"),
    path("login/", views.login, name="login"), 
    path("my-account/", views.my_account, name="my_account"),
    # path("password/", auth_views.PasswordChangeView.as_view(template_name='change-password.html')),#djangonun oz viewsu ile
    path("password/", views.PasswordsChangeView.as_view(template_name='change-password.html')),
    path('password_success/', views.password_success, name="password_success"),
    
]
