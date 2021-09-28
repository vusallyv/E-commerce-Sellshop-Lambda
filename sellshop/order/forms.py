from django import forms
from order.models import Billing


class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        exclude = ('user_id'),
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder':'Company name here...'}),
            'country': forms.TextInput(attrs={'placeholder':'Country'}),
            'state': forms.TextInput(attrs={'placeholder':'State'}),
            'city': forms.TextInput(attrs={'placeholder':'City'}),
            'address': forms.Textarea(attrs={'rows': 2, 'placeholder':'Order notes here...'}),
        }