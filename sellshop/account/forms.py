from django import forms
from account.models import User
from django.contrib.auth import get_user_model


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('email', 'password')

#         widgets = {
#             'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
#             'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
#         }

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email Address..'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))

    def clean(self):
        user = User.objects.filter(email=self.cleaned_data.get('email')).first()
        if not user:
            raise forms.ValidationError('Invalid Username')
        if not user.check_password(self.cleaned_data['password']):
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

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError("Email already in use")
    #     return email

    # def clean(self):
    #     data = super().clean()
    #     password = data['password']
    #     confirm_password = data['confirm_password']
    #     if password == confirm_password:
    #         raise forms.ValidationError("Password confirmation does not match")
    #     return data
