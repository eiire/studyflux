from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from index_page.models import Portfolios


class PortfolioForm(ModelForm):
    # server side validation
    def clean_name(self):
        data = self.cleaned_data['name']
        if len(data) > 30 or len(data) <= 0:
            raise ValidationError

        # return clean data
        return data

    class Meta:
        model = Portfolios
        fields = ['name', 'image', 'topics']


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