from django.shortcuts import redirect, redirect, render

# Create your views here.

from account.models import User
from account.forms import LoginForm, RegisterForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
import random


def contact(request):
    context = {
        'title':  'Contact Us Sellshop'
    }
    return render(request, "contact.html", context=context)


def login(request):
    auth.logout(request)
    if request.method == "POST" and 'register' in request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=request.POST.get('email')).exists() == False:
                if User.objects.filter(phone_number=request.POST.get('phone_number')).exists() == False:
                    if request.POST.get('password') == request.POST.get('confirm_password'):
                        random_number = random.randint(0, 10000)
                        while User.objects.filter(username=f"Guest_{random_number}"):
                            random_number = random.randint(0, 1000000)
                        user = User(
                            first_name=request.POST.get('first_name'),
                            email=request.POST.get('email'),
                            phone_number=request.POST.get('phone_number'),
                            password=request.POST.get('password'),  
                            username=f"Guest_{random_number}",
                        )
                        user.save()
                        auth.login(request, user)
                        return redirect(my_account)
                    else:
                        raise 'Password must be same'
                else:
                    raise 'Phone number already in use'
            else:
                raise 'Email already in use'
    else:
        form = RegisterForm()
    
    if request.method == "POST" and 'login' in request.POST:
        form = RegisterForm(request.POST)
        auth.login(request, User.objects.get(email=request.POST.get('email')))
        return redirect(my_account)
        # else:   
        #     raise "Email not found"
    context = {
        'title':  'Login Sellshop',
        'login':  LoginForm,
        'register':  RegisterForm,
    }
    return render(request, "login.html", context=context)


# @login_required(login_url='/account/my-account/')
def my_account(request):
    context = {
        'title':  'My-account Sellshop'
    }
    if request.user.is_authenticated:
        return render(request, "my-account.html", context=context)
    else:
        return render(request, "error-404.html", context=context)
