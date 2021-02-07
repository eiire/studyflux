from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class CustomAuthForm(AuthenticationForm):
    username = UsernameField(
        label=False,
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'id': 'login',
            'class': 'fade_in second mt-5',
            'name': 'login',
            'placeholder': 'login'
        })
    )
    password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'id': 'password',
            'class': 'fade_in third',
            'name': 'password',
            'placeholder': 'password'
        }),
    )
