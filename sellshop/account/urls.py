from django.urls import path
from . import views

urlpatterns = [
    path("contact/", views.ContactView.as_view(), name="contact"), # HTML de istifade etmek ucun
    path("login/", views.login, name="login"),
    path("my-account/", views.my_account, name="my_account"),
]