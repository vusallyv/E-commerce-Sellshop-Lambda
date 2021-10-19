from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

# Create your views here.

from django.urls import reverse_lazy
from user.forms import ContactForm, LoginForm, RegisterForm, SubscriberForm
from user.models import User, Contact
from django.contrib import auth
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
import random


User = auth.get_user_model()



class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'password_success.html', {})


class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    model = Contact
    success_url = reverse_lazy('contact')


def contact(request):
    if request.method == 'POST' and "contact" in request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()

    if request.method == 'POST' and 'subscribe' in request.POST:
        subscribe = SubscriberForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('contact')
    else:
        subscribe = SubscriberForm()


    context = {
        'title':  'Contact Us Sellshop',
        'contactform': form,
        'subscribeform': subscribe,
    }
    return render(request, "contact.html", context=context)


def login(request):
    if request.method == "POST" and 'register' in request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            random_number = random.randint(0, 10000)
            while User.objects.filter(username=f"Guest_{random_number}"):
                random_number = random.randint(0, 1000000)
            user = User(
                first_name=request.POST.get('first_name'),
                email=request.POST.get('email'),
                phone_number=request.POST.get('phone_number'),
                username=f"Guest_{random_number}",
                rememberme=request.POST.get('rememberme'),
            )
            user.set_password(request.POST.get('password')),
            user.save()
            auth.login(request, user)
            return redirect(my_account)
    else:
        form = RegisterForm()

    if request.method == "POST" and 'login' in request.POST:
        form1 = LoginForm(request.POST)
        user = User.objects.filter(email=request.POST.get('email')).first()
        if user is not None and user.check_password(request.POST.get('password')):
            auth.login(request, user)
            return redirect(my_account)
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


# @login_required(login_url='/account/my-account/')
def my_account(request):
    context = {
        'title':  'My-account Sellshop'
    }
    if request.user.is_authenticated:
        return render(request, "my-account.html", context=context)
    else:
        return render(request, "error-404.html", context=context)
