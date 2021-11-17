from django import forms
from order.models import Billing, ShippingAddress


class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        exclude = ('user',)
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'Company name here...'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
        }


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        exclude = ('user',)
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'Company name here...'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
        }
