from django import forms
from product.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'review']
