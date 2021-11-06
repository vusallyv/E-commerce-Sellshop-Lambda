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
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email...'})
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your Name...'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email...'}),
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
        attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email Address..', "id": "email"}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Phone Number..'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', "id": "password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))
    CHOICES = [('1', 'Sign up for our newsletter!'), ]
    rememberme = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Phone number already in use")
        elif len(str(phone_number)) > 10:
            raise forms.ValidationError("Invalid phone number")
        return phone_number

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already in use")
        return username
    
    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     password_confirm = self.cleaned_data.get('confirm_password')
    #     if not (password == password_confirm):
    #         raise forms.ValidationError("Password confirmation does not match")
    #     return password


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', ]

        widgets = {
            'email': TextInput(attrs={'placeholer': 'Enter your email...'}),
        }
