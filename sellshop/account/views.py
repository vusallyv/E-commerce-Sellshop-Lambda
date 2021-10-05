from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from account.forms import ContactForm, LoginForm, RegisterForm
from account.models import User, Contact
from django.contrib import auth
from django.views.generic import CreateView
import random
from django.views.generic.edit import FormView

User = get_user_model()

class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    model = Contact
    success_url = reverse_lazy('login') 

# class ContactView(FormView):
#     template_name = 'contact.html'
#     form_class = ContactForm
    
#     def post(self, request, *args, **kwargs):
#         self.object = None
#         if request.method == 'POST':
#             form = ContactForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 form = ContactForm()
#         else:
#             form = ContactForm()
#             form.send_email()
#         return super().post(request, *args, **kwargs)
    


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


# def logout_user(request):
#     if request.user.is_authenticated():
#         logout(request)
#         return redirect('login')


# @login_required(login_url='/account/my-account/')
def my_account(request):
    context = {
        'title':  'My-account Sellshop'
    }
    if request.user.is_authenticated:
        return render(request, "my-account.html", context=context)
    else:
        return render(request, "error-404.html", context=context)
