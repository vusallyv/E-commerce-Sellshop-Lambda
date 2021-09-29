from django import forms
from django.forms import widgets
from account.models import Contact 



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
        
        
        

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



        
        
    