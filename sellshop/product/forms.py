from django import forms
from product.models import Review
# from django.contrib.flatpages.forms import FlatpageForm
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review', 'rating')

        widgets = {
            'review': forms.Textarea(attrs={'placeholder': 'Your Review', 'rows': 2}),
        }
# class FlatpageCustomForm(FlatpageForm):
#     content = forms.CharField(widget=CKEditorUploadingWidget())