from django import forms
from django.forms import widgets
from product.models import Review 


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product_id', 'review']
        