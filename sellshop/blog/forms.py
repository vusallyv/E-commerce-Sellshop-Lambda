from django import forms
from blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description',]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Comment here'}),
        }
