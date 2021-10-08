from django.shortcuts import render, redirect

# Create your views here.

from django.urls import reverse_lazy
from user.forms import ContactForm, LoginForm, RegisterForm
from user.models import User, Contact
from django.contrib import auth
from django.views.generic import CreateView
import random
# from django.contrib.auth.decorators import login_required

User = auth.get_user_model()


class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    model = Contact
    success_url = reverse_lazy('login')


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
