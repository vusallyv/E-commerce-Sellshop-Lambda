from django import forms
from product.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description', 'blog_id']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Comment here'}),
        }

