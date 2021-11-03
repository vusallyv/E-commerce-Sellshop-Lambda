from django import forms
from order.models import Billing, ShippingAddress


class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        exclude = ('user',),
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder':'Company name here...'}),
            'state': forms.TextInput(attrs={'placeholder':'State'}),
            'city': forms.TextInput(attrs={'placeholder':'City'}),
            'address': forms.TextInput(attrs={'placeholder':'Address'}),
        }


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        exclude = ('user',)
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name here...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name here...'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone number here...'}),
            'company_name': forms.TextInput(attrs={'placeholder': 'Company name here...'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
        }
        
