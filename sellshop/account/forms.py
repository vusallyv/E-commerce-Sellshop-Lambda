from django import forms
from django.forms.widgets import DateInput
from account.models import User
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email Address..'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))

    def clean(self):
        user = User.objects.filter(
            email=self.cleaned_data.get('email')).first()
        if not user:
            raise forms.ValidationError('Invalid Username')
        if not user.check_password(self.cleaned_data.get('password')):
            raise forms.ValidationError('Invalid Password')
        return self.cleaned_data


class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Name here..'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email Address..'}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Phone Number..'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))
    CHOICES = [('1', ' '), ]
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
        return phone_number

    def clean(self):
        data = super().clean()
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password == confirm_password:
            raise forms.ValidationError("Password confirmation does not match")
        return data


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('__all__')

        widgets = {
            'birth': DateInput(attrs={'type': 'date'}),
        }
