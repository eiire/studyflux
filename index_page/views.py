from django.shortcuts import render, redirect
from index_page.models import Portfolios
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .form import ReviewForm


# Create your views here.
def get_startpage(request):
    """Получить главную страницу"""
    if request.user.username != '':
        user_id = User.objects.get(username=request.user).pk
        return redirect('get_userpage', user_portfolios=user_id)
    else:
        portfolios = Portfolios.objects.all()
        context = {
            'portfolios': portfolios,
            'user': False
        }
        return render(request, "index.xhtml", context)


def get_userpage(request, user_portfolios):
    """Получить страницу с текущим пользователем"""
    user_portfolio = Portfolios.objects.filter(user_id=user_portfolios)
    context = {
        'portfolios': user_portfolio,
        'user': True
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
