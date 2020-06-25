from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, NoReverseMatch
from django.views.generic import FormView

from blog.models import Category, Post
from index_page.models import Portfolios
from projects.forms import ProjectForm
from projects.models import Project


class CreatorProjectView(FormView, LoginRequiredMixin):
    form_class = ProjectForm
    template_name = 'project_creator.html'
    success_url = reverse_lazy('index')

    def get(self, request, user_id, name_portfolio):
        try:
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
            self.field_knowledge = current_portfolios
            current_portfolios.topics += 1
            current_portfolios.save()
        except ObjectDoesNotExist:
            return HttpResponse(status=404)

        if request.user.id == int(user_id):
            self.user_id = request.user.id
            return super().post(request, user_id)
        else:
            return redirect('project_creator', request.user.id)

    def form_valid(self, form):
        new_category = Project(
            title=form["title"].value(),
            description=form["description"].value(),
            user_portfolio=self.field_knowledge
        )
        new_category.save()
        Category(name=form["title"].value(), user=self.request.user, project=new_category).save()
        return super(CreatorProjectView, self).form_valid(form)


def project_index(request, user_id, name_portfolio):
    projects = Project.objects.filter(user_portfolio=name_portfolio)
    count_articles_project = [Post.objects.filter(categories__name__contains=Category.objects.get(project=project).name).count() for project in projects]
    projects = zip(projects, count_articles_project)
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
