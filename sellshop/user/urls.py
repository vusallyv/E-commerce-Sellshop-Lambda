from django.conf.urls import include
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
     path("contact/", views.contact, name="contact"),
     # path("contact/", views.ContactView.as_view(), name="contact"),
     path("login/", views.login, name="login"),
     path("my-account/", views.my_account, name="my_account"),
     path('logout/', views.logout, name="logout"),
     path('accounts/', include('allauth.urls')),
     path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),
          name="password_reset"),
     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
          name="password_reset_done"),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
          name="password_reset_confirm"),
     path('password_reset/complete', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
          name="password_reset_complete"),
     path("password/", auth_views.PasswordChangeView.as_view(template_name='change-password.html')),
     # path("password/", views.PasswordsChangeView.as_view(template_name='change-password.html')),
     # path('password_success/', views.password_success, name="password_success"),
     path("contact/", views.ContactSubscripView.as_view(), name="contact"),
]