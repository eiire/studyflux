from django.contrib.auth.views import LoginView
from my_portfolio.forms import CustomAuthForm


class CustomDjangoLoginView(LoginView):
    form_class = CustomAuthForm
