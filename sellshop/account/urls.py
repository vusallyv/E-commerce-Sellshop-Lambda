from django.urls import path
from . import views

urlpatterns = [
    path("contact/", views.contact, name="contact"), # HTML de istifade etmek ucun
    path("login/", views.login, name="login"),
    path("my-account/", views.my_account, name="my_account"),
    path("login-practic/", views.login_user, name="login_practic"),
    path("logout/", views.logout_user, name="logout"),
]