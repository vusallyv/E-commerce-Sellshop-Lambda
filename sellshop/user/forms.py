from django.db.models.query_utils import Q
from user.models import Subscriber, User, Contact
from django.forms.widgets import TextInput
from django import forms
from user.models import Contact, Subscriber
from django.contrib.auth import get_user_model

User = get_user_model()


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email...', "style": "width: 100% !important;"})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'birth', 'image']

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone number: 0123456789'}),
            'birth': forms.DateInput(attrs={'type': 'date'})
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your Name...'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email...', "id": "contactEmail"}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message....', 'rows': 2}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username..'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))

    def clean(self):
        user = User.objects.filter(
            username=self.cleaned_data.get('username')).first()
        if not user:
            raise forms.ValidationError('Invalid Username')
        if not user.check_password(self.cleaned_data.get('password')):
            raise forms.ValidationError('Invalid Password')
        return self.cleaned_data


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', "id": "username"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email Address..', "id": "email"}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Phone Number..'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', "id": "password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(Q(email=email) & Q(is_active=True)).exists():
            raise forms.ValidationError('The email is already in use')
        elif User.objects.filter(Q(email=email) & Q(is_active=False)).exists():
            User.objects.filter(email=email).delete()
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(Q(username=username) & Q(is_active=True)).exists():
            raise forms.ValidationError('The username is already in use')
        elif User.objects.filter(Q(username=username) & Q(is_active=False)).exists():
            User.objects.filter(username=username).delete()
        return username

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if User.objects.filter(Q(phone_number=phone_number) & Q(is_active=True)).exists():
            raise forms.ValidationError('The phone number is already in use')
        elif User.objects.filter(Q(phone_number=phone_number) & Q(is_active=False)).exists():
            User.objects.filter(phone_number=phone_number).delete()
        return phone_number

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                'Password confirmation does not match.')
        elif len(password) < 8:
            raise forms.ValidationError(
                'Password must be at least 8 characters long')
        elif password.isdigit():
            raise forms.ValidationError(
                'Password must contain at least one letter')
        elif password.isalpha():
            raise forms.ValidationError(
                'Password must contain at least one number')
        elif password.islower():
            raise forms.ValidationError(
                'Password must contain at least one upper case letter')
        elif password.isupper():
            raise forms.ValidationError(
                'Password must contain at least one lower case letter')
        elif password.isspace():
            raise forms.ValidationError(
                'Password must not contain any spaces')
        elif password.isalnum():
            raise forms.ValidationError(
                'Password must contain at least one special character')
        return confirm_password
