from django import forms
from django.forms import ModelForm
from blog.models import Post


class ArticleCreatorForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'title', 'image']  # 'user', 'title', 'categories']


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )