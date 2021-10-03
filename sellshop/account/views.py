from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login,logout
from account.forms import ContactForm, UserRegisterForm, UserLoginForm
from account.models import UserProfile
from django.db import transaction

User = get_user_model()


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()
    context = {
        'title':  'Contact Us Sellshop',
        'form': ContactForm(),
    }
    return render(request, "contact.html", context=context)


def login(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = User(
                    email=form.cleaned_data.get('email'),
                    first_name=form.cleaned_data.get('first_name'),
                    last_name=form.cleaned_data.get('last_name'),
                    )
                user.set_password(form.cleaned_data.get('password'))
                user.save() 
                user_profile = UserProfile.objects.create(
                    user=user,
                    country = form.cleaned_data.get('country'),
                    address = form.cleaned_data.get('address'),
                    city = form.cleaned_data.get('city'),
                    phone_number = form.cleaned_data.get('phone_number'),
                    additional_info = form.cleaned_data.get('additional_info'),
                    )
        else:   
            form = UserRegisterForm()
            
    context = {
        'title':  'Login Sellshop',
        'form': UserRegisterForm(),
    }
    return render(request, "login.html", context=context)


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data.get('email')).first()
            login(request, user)
    else:
        form = UserLoginForm()
    context = {
        'title':  'Login Sellshop',
        'form': UserLoginForm(),
    }

    return render(request, "login_practic.html", context=context)


def logout_user(request):
    if request.user.is_authenticated():
        logout(request)
        return redirect('login')


def my_account(request):
    context = {
        'title':  'My-account Sellshop'
    }
    return render(request, "my-account.html", context=context)