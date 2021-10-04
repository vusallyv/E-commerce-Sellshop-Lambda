from django import forms
from product.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']

        widgets = {
            'review': forms.Textarea(attrs={'placeholder': 'Your Review', 'rows': 2})
        }
