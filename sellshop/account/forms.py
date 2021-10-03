from django import forms
from django.forms import widgets
from account.models import Contact
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        
     
class UserRegisterForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    country = forms.CharField(label='Country')
    address = forms.CharField(label='Address')
    city = forms.CharField(label='City')
    phone_number = forms.CharField(label='Phone Number')
    additional_info = forms.CharField(label='AdditionalInfo')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirmation = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The email is already in use')
        return email
    
    def clean(self):
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Password confirmation does not match.')
        return data
        
        
class UserLoginForm(forms.Form):
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    def clean(self):
        user = User.objects.filter(email=self.cleaned_data['email']).first()
        if not user:
            raise forms.ValidationError('user does not exist.')
        if not user.check_password(self.cleaned_data['password']):
            raise forms.ValidationError('password is incorrect.')
        return self.cleaned_data



# forms.Form istifade usulu

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Enter your name'})
#     )
#     email = forms.EmailField(max_length=150, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
#     )
#     message = forms.CharField(max_length=1000, widget=forms.TextInput(
#         attrs={'class':'form-control', 'placeholder': 'Enter your message'})
#     )
    
#     def clean_name(self):
#         data = self.cleaned_data['name']
#         if len(data) < 4:
#             raise forms.ValidationError('Name len error')
#         return data



        
        
    