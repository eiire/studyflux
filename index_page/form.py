from django import forms
from django.contrib.auth.models import User


class PortfolioForm(forms.Form):
    name_portfolio = forms.CharField(
        initial="Portfolio"
    )
    short_description = forms.CharField(
        min_length=0,
        max_length=100
    )


class CreateUser(forms.Form):
    login = forms.CharField(
        initial="Login"
    )
    password = forms.CharField(
        initial="Password"
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