from django.db.models.expressions import F
from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.db import transaction

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, View
from order.forms import BillingForm
from order.models import Billing, Cart, City, Country
from user.forms import ContactForm, LoginForm, RegisterForm, SubscriberForm, UserForm
from user.models import User, Contact, Subscriber
from django.contrib import auth
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
import random
from user.tasks import send_mail_to_users

from datetime import datetime

User = auth.get_user_model()


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'password_success.html', {})


def contact(request):
    context = {
        'title':  'Contact Us Sellshop',
    }
    return render(request, "contact.html", context=context)


def login(request):
    auth.logout(request)
    if request.method == "POST" and 'register' in request.POST:
        form = RegisterForm(request.POST)
        with transaction.atomic():
            user = User(
                username=request.POST.get('username').lower(),
                email=request.POST.get('email').lower(),
                first_name=request.POST.get('first_name'),
                phone_number=request.POST.get('phone_number'),
            )
            user.set_password(request.POST.get('password'))
            user.save()

        auth.login(request, user)
        return redirect('my_account')
    else:
        form = RegisterForm()

    if request.method == "POST" and 'login' in request.POST:
        form1 = LoginForm(request.POST)
        user = User.objects.filter(
            username=request.POST.get('username').lower()).first()
        if user is not None and user.check_password(request.POST.get('password')):
            auth.login(request, user)
            return redirect('my_account')
    else:
        form1 = LoginForm()

    context = {
        'title':  'Login Sellshop',
        'login':  form1,
        'register':  form,
    }
    return render(request, "login.html", context=context)


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('login')


def my_account(request):
    message = ''
    success = False
    if request.method == "POST" and "billing" in request.POST:
        billing = BillingForm(request.POST)
        if billing.is_valid():
            if Billing.objects.filter(user=request.user).exists() == False:
                billing = Billing(
                    user=request.user,
                    company_name=request.POST.get('company_name'),
                    country=Country.objects.get(
                        id=request.POST.get('country')),
                    city=City.objects.get(id=request.POST.get('city')),
                    address=request.POST.get('address'),
                )
                billing.save()
                message = 'Billing information added successfully'
            else:
                Billing.objects.filter(user=request.user).update(
                    company_name=request.POST.get('company_name'),
                    country=Country.objects.get(
                        id=request.POST.get('country')),
                    city=City.objects.get(id=request.POST.get('city')),
                    address=request.POST.get('address')
                )
                message = 'Billing information updated successfully'
            success = True
        else:
            message = 'Invalid Billing information'
    else:
        billing = BillingForm()

    if request.method == "POST" and "account_info" in request.POST:
        user_info = UserForm(request.POST)
        if user_info.is_valid():
            request.user.first_name = request.POST.get('first_name')
            request.user.last_name = request.POST.get('last_name')
            request.user.phone_number = request.POST.get('phone_number')
            request.user.birth = request.POST.get('birth')
            request.user.image = f"users/{request.POST.get('image')}"
            request.user.save()
            message = 'Account information updated successfully'
            success = True
        else:
            message = 'Invalid account information'
    else:
        user_info = UserForm()
    context = {
        'title':  'My-account Sellshop',
        'billing': billing,
        'user_info': user_info,
        'orders': Cart.objects.filter(Q(user=request.user) & Q(
            is_ordered=True)),
        'message': message,
        'success': success,
    }
    if request.user.is_authenticated:
        return render(request, "my-account.html", context=context)
    else:
        return render(request, "error-404.html", context=context)


def send_mail_to_subscribers_view(request):
    send_mail_to_subscribers.delay()
    return render(request, "subscriber_mail.html")
