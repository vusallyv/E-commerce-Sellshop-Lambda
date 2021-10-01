from django.shortcuts import redirect, render

# Create your views here.

from account.models import User
from account.forms import LoginForm, RegisterForm
from django.contrib import auth
import random
# from django.contrib.auth.decorators import login_required


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
        form = RegisterForm(request.POST)
        user = User.objects.filter(email=request.POST.get('email')).first()
        if user is not None and user.check_password(request.POST.get('password')):
            auth.login(request, user)
            return redirect(my_account)
    else:
        form = LoginForm(request.POST)

    context = {
        'title':  'Login Sellshop',
        'login':  LoginForm,
        'register':  RegisterForm(request.POST),
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
