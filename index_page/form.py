from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from blog.models import Post


class PortfolioForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body']


class LoginUser(forms.Form):
    login = forms.CharField(
        initial="Login"
    )

    password = forms.CharField(
        widget=forms.PasswordInput
    )


class ReviewForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        if not user.is_authenticated:
            self.fields['first_name'] = forms.CharField(
                initial="Anonymous"
            )
            self.fields['last_name'] = forms.CharField(
                initial="User"
            )
        else:
            self.fields['first_name'] = forms.CharField(
                initial=user.first_name
            )
            self.fields['last_name'] = forms.CharField(
                initial=user.last_name
            )