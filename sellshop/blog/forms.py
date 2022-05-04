from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def clean_reply(self):
        if self.cleaned_data['reply'] == self.instance:
            raise forms.ValidationError("Reply cannot be same as comment.")
        return self.cleaned_data['reply']
