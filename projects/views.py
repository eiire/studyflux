from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from blog.models import Category, Post
from index_page.models import Portfolios
from projects.models import Project


class CreateTopic(LoginRequiredMixin, CreateView):
    model, fields = Project, '__all__'
    template_name = 'project_creator.html'

    def get_form(self, **kwargs):
        form_class = self.get_form_class()
        form = form_class(**self.get_form_kwargs())
        form.fields['user_portfolio'].queryset = Portfolios.objects.filter(user=self.request.user)
        form.fields['user_portfolio'].label_from_instance = lambda obj: "%s" % obj.name
        # print(form['user_portfolio'], form.fields['user_portfolio'])  # Form Field and him BoundField
        return form

    def get_success_url(self, **kwargs):
        return reverse("project_index", args=self.kwargs.values())

    def form_valid(self, form):
        self.object = form.save()
        Category(name=form["title"].value(), user=self.request.user, project=self.object).save()
        return super().form_valid(form)


class Topics(ListView):
    template_name = 'project_index.html'

    def get_queryset(self):
        projects = Project.objects.filter(user_portfolio=self.kwargs['id_knowledge'])
        count_articles_project = [
            Post.objects.filter(categories__id__contains=Category.objects.get(project=project).id).count()
            for project in projects
        ]
        projects = zip(projects, count_articles_project)
        return projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user.is_authenticated
        context['user_id'] = self.kwargs.get('user_id')
        context['id_knowledge'] = self.kwargs.get('id_knowledge')
        # context['user_auth'] = self.request.user.is_authenticated
        return context


def project_detail(request, user_id, name_portfolio, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'user_id': user_id,
        'user_auth': request.user.is_authenticated,
        'id_knowledge': name_portfolio,
        'project': project,
    }
    return render(request, 'project_detail.html', context)
