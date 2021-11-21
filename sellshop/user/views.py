from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
# Create your views here.

from django.urls import reverse_lazy
from django.contrib import auth
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from user.tasks import send_mail_to_users
from django.utils.encoding import force_bytes, force_text
from django.http import HttpResponse
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from sellshop.settings import EMAIL_HOST_USER

from order.forms import BillingForm
from order.models import Billing, Cart, City, Country
from user.forms import LoginForm, RegisterForm, UserForm

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
    message = ''
    auth.logout(request)
    if request.method == "POST" and 'register' in request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data.get('username'),
                first_name=form.cleaned_data.get('first_name'),
                email=form.cleaned_data.get('email'),
                phone_number=form.cleaned_data.get('phone_number'),
            )
            user.set_password(form.cleaned_data.get('password'))
            user.is_active = False
            user.save()
            message = 'Your account has been created successfully. Please check your email to activate your account.'
            verify_email(request, user=user, to_email=user.email)
    else:
        form = RegisterForm()

    if request.method == "POST" and 'login' in request.POST:
        form1 = LoginForm(request.POST)
        user = User.objects.filter(
            username=request.POST.get('username').lower()).first()
        if user is not None and user.check_password(request.POST.get('password')):
            if user.is_active:
                auth.login(request, user)
                return redirect('my_account')
            else:
                message = 'Please verify your email address to login'
        else:
            message = 'Invalid username or password'
    else:
        form1 = LoginForm()

    context = {
        'title':  'Login Sellshop',
        'login':  form1,
        'register':  form,
        'message': message,
    }
    return render(request, "login.html", context=context)


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('login')

def my_account(request, verify_message=None):
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
    return render(request, "error-404.html", context=context)


def send_mail_to_subscribers_view(request):
    send_mail_to_users.delay()
    return render(request, "subscriber_mail.html")



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # my_account(request, verify_message='Your account has been activated successfully.')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def verify_email(request, user, to_email):
    current_site = get_current_site(request)
    body = render_to_string('verification_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    msg = EmailMessage(subject='Activate your account.', body=body,
                        from_email=EMAIL_HOST_USER,
                        to=[to_email, ])
    msg.content_subtype = 'html'
    msg.send(fail_silently=True)