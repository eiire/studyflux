from django import forms
from django.forms import ModelForm, models
from blog.models import Post, Category
from index_page.models import Portfolios


class ArticleCreatorForm(ModelForm):
    """ Post model-form extended Category model-form. """

    def __init__(self, user_id, *args, **kwargs):
        super(ArticleCreatorForm, self).__init__(*args, **kwargs)
        # bound method ModelChoiceField.label_from_instance of django.forms.models.ModelMultipleChoiceField
        self.fields['categories'].label_from_instance = lambda obj: "%s" % obj.name
        self.fields['categories'].queryset = Category.objects.filter(user_id=user_id)

        self.fields.update({'new_category': forms.fields.CharField(
            required=False,
            label='New Category',
            help_text='(not required)'
        )})

        self.fields.update({'field_knowledge': models.ModelMultipleChoiceField(
            queryset=Portfolios.objects.filter(user=user_id),
            label='Choose a field of knowledge:',
            widget=forms.RadioSelect(attrs={'id': 'field_knowledge'})
        )})
        self.fields['field_knowledge'].label_from_instance = lambda obj: "%s" % obj.name

    class Meta:
        model = Post
        fields, exclude = '__all__', ['user']

        widgets = {
            'categories': forms.CheckboxSelectMultiple(attrs={'id': 'categories'}),
            'header': forms.Textarea(attrs={'cols': '100', 'rows': '5', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'type': 'file', 'class': 'form-control-file'}),
            # 'new_category': forms.TextInput(attrs={'required': 'False'}),
        }

        labels = {
            'categories': 'Please equip the category this post',
        }

        help_texts = {
            'categories': '(not required)',
        }


class FieldKnowledgeFprm():
    pass


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
