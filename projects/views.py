from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, NoReverseMatch
from django.views.generic import FormView

from index_page.models import Portfolios
from projects.forms import ProjectForm
from projects.models import Project


class CreatorProjectView(FormView, LoginRequiredMixin):
    user_id = None
    name_portfolio = None
    form_class = ProjectForm
    template_name = 'project_creator.html'
    success_url = reverse_lazy('index')

    def get(self, request, user_id, name_portfolio):
        try:
            # portfolio <- project
            user_portfolios = Portfolios.objects.filter(user=request.user)
            current_portfolios = user_portfolios.get(id=name_portfolio)
            self.name_portfolio = current_portfolios
        except ObjectDoesNotExist:
            return HttpResponse(status=404)

        if request.user.id == int(user_id):
            self.user_id = request.user.id
            return super().get(request, user_id)
        else:
            return redirect('project_creator', request.user.id)

    def post(self, request, user_id, name_portfolio):
        try:
            user_portfolios = Portfolios.objects.filter(user=request.user)
            current_portfolios = user_portfolios.get(id=name_portfolio)
            self.name_portfolio = current_portfolios
            current_portfolios.count_proj += 1
            current_portfolios.save()
        except ObjectDoesNotExist:
            return HttpResponse(status=404)

        if request.user.id == int(user_id):
            self.user_id = request.user.id
            return super().post(request, user_id)
        else:
            return redirect('project_creator', request.user.id)

    def get_initial(self):
        return {
            'user_portfolio': self.name_portfolio.pk
        }

    def form_valid(self, form):
        new_portfoio = Project(
            user_portfolio_id=self.name_portfolio.pk,
            title=form["title"].value(),
            technology=form["technology"].value(),
            github=form["github"].value(),
            name_for_portfolios=form["name_for_portfolios"].value(),
        )
        new_portfoio.save()
        return super(CreatorProjectView, self).form_valid(form)


def project_index(request, user_id, name_portfolio):
    projects = Project.objects.filter(user_portfolio=name_portfolio)
    context = {
        'user': request.user.is_authenticated,
        'user_id': user_id,
        'user_auth': request.user.is_authenticated,
        'projects': projects,
        'name_portfolio': name_portfolio,
    }
    return render(request, 'project_index.html', context)


def project_detail(request, user_id, name_portfolio, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'user_id': user_id,
        'user_auth': request.user.is_authenticated,
        'name_portfolio': name_portfolio,
        'project': project,
    }
    return render(request, 'project_detail.html', context)
