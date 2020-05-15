from django.shortcuts import render, redirect
from index_page.models import Portfolios
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .form import ReviewForm, CreateUser


# Create your views here.
def get_startpage(request):
    """Получить главную страницу"""
    if request.user.username != '':
        user_id = User.objects.get(username=request.user).pk
        return redirect('get_userpage', user_portfolios=user_id)
    else:
        if request.method == 'GET':
            portfolios = Portfolios.objects.all()
            context = {
                'portfolios': portfolios,
                'user': False,
                'user_name': 'anon',
                'auth_form': CreateUser
            }
            return render(request, "index.xhtml", context)
        if request.method == 'POST':
            print(request.POST)  # обработать форму аутентификации
            return render(request, "index.xhtml")


def get_userpage(request, user_portfolios):
    print(user_portfolios)
    """Получить страницу с текущим пользователем"""
    user_portfolio = Portfolios.objects.filter(user_id=user_portfolios)
    context = {
        'portfolios': user_portfolio,
        'user': True,
        'user_name': user_portfolios
    }
    return render(request, "index.xhtml", context)


class CreatePortfolio(View, LoginRequiredMixin):
    """Создание/редактирование портфолио для зарегестрированного пользователя"""
    def get(self, request):
        form = ReviewForm(request.user)
        print(form.fields)
        return render(request, 'port_form.html', {'form': form})


def about(request):
    return render(request, "about.xhtml")
