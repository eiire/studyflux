from django import forms
from django.forms import ModelForm, BaseModelFormSet
from blog.models import Post, Category


class ArticleCreatorForm(ModelForm):
    # Other implementation in Bookmarks/Study/Django/to_field_name
    def __init__(self, user_id, *args, **kwargs):
        super(ArticleCreatorForm, self).__init__(*args, **kwargs)
        self.queryset = Post.objects.filter(categories__name='d')
        self.fields['categories'].label_from_instance = lambda obj: "%s" % obj.name
        self.fields['categories'].queryset = Category.objects.filter(user_id=user_id)

    class Meta:
        model = Post
        fields = '__all__'  # 'user']

        widgets = {
            'categories': forms.SelectMultiple(attrs={'id': 'add_id_categories', 'size': '5', 'class': 'form-control'}),
            'header': forms.Textarea(attrs={'cols': '100', 'rows': '5', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'type': 'file', 'class': 'form-control-file'})
        }


class CategoryCreatorForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'required': False}),
        }

        labels = {
            'name': 'New category',
        }

        help_texts = {
            'name': 'Some useful help text.',
        }


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