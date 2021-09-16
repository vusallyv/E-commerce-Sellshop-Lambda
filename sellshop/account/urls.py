from django.urls import path
from . import views

urlpatterns = [
    path("contact/", views.contact, name="contact"), # HTML de istifade etmek ucun
    path("login/", views.login, name="login"),
    path("my_account/", views.my_account, name="my_account"),
]