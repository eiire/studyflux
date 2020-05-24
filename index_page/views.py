from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView

from index_page.models import Portfolios
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from projects.models import Project
from .forms import ReviewForm, LoginUser, PortfolioForm


def get_startpage(request):
    """Получить главную страницу"""
    if request.user.username != '':
        user_id = User.objects.get(username=request.user).pk
        return redirect('get_userpage', user_id=user_id)
    else:
        form = LoginUser(request.POST)

        context = {
            'portfolios': Portfolios.objects.all(),
            'user': False,
            'user_id': 'anon',
            'auth_form': form,
            'is_user': request.user.is_authenticated,
        }

        if request.method == 'GET':
            return render(request, "index.html", context)
        elif request.method == 'POST':
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['login'], password=cd['password'])

                if user is not None:
                    if user.is_active:
                        login(request, user)
                        user_id = User.objects.get(username=request.user).pk
                        return redirect('get_userpage', user_id=user_id)
                    else:
                        return HttpResponse('Disabled account')
                else:
                    return HttpResponse('Invalid login')

            return render(request, "index.html")


def portfolio_dlt(request, user_id, pk):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(id=request.user.pk)
            posts = Portfolios.objects.filter(user=user)
            post = posts.get(id=pk)
            post.delete()

            return redirect("index")
        except ObjectDoesNotExist:
            return HttpResponse(status=401)
    else:
        return redirect("login")


def get_userpage(request, user_id):
    """Получить страницу с текущим пользователем"""
    user_portfolio = Portfolios.objects.filter(user_id=user_id)
    context = {
        'portfolios': user_portfolio,
        'user': True,
        'user_id': user_id
    }
    return render(request, "index.html", context)


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"

    template_name = "register.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)


class CreatePortfolio(View, LoginRequiredMixin):
    """Создание/редактирование портфолио для аутентефицированного пользователя"""
    def get(self, request, user_id):
        form = PortfolioForm()
        return render(request, 'port_form.html', {'form': form})

    def post(self, request, user_id):
        form = PortfolioForm(request.POST)  # binding
        try:
            form.is_valid()
        except:
            return HttpResponse(status=401)

        new_portfolio = Portfolios(
            user=request.user,
            name=form.data['name'],
            count_proj=0,
            contacts=form.data['contacts'],
            image=request.FILES['image']
        )
        new_portfolio.save()
        return redirect('get_userpage', request.user.id)


def about(request):
    return render(request, "about.xhtml")
