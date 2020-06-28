from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, ListView, DeleteView
from blog.models import Post
from index_page.models import Portfolios
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class StartPageView(ListView):
    template_name = "index.html"
    context_object_name, extra_context = 'knowledges', {'user_id': 'global'}
    queryset = Portfolios.objects.filter(user_id=1)  # 1 is global knowledges

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['user'] = self.request.user
        return context


class UserPageView(StartPageView):
    def get_queryset(self):
        if self.request.user.id != self.kwargs.get('user_id'):
            user_knowledges = Portfolios.objects.filter(user_id=self.kwargs['user_id'])
            return user_knowledges if user_knowledges.count() != 0 else None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.id == self.kwargs.get('user_id'):
            context['posts'] = Post.objects.all()  # [task] Select by subscription
        else:
            context['posts'] = Post.objects.filter(user_id=self.kwargs.get('user_id'))

        context['user_id'] = self.kwargs.get('user_id')
        return context


# TOPICS
class KnowledgePageView():
    pass


# TOPICS
class UserKnowledgePageView():
    pass


class UserProfile():
    pass


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class CreateKnowledge(View, LoginRequiredMixin):
    def get(self, request, **kwargs):
        knowledge_img = {
            'all-streams': 'portfolio/1.png',
            'Development': 'portfolio/1.png'
        }
        all_knowledge = ['all-streams', 'Development']
        user_knowledge = [el['name'] for el in Portfolios.objects.filter(user=request.user.id).values('name')]

        if kwargs.get('knowledge') in all_knowledge and kwargs.get('knowledge') not in user_knowledge:
            Portfolios(user=request.user, name=kwargs['knowledge'], topics=0, image=knowledge_img[kwargs['knowledge']])\
                .save()

        return redirect('index_user', self.request.user.id)


class DeleteKnowledge(DeleteView, LoginRequiredMixin):
    model = Portfolios
    template_name = 'knowledge_confirm_delete.html'

    def get_queryset(self):
        return Portfolios.objects.filter(user=self.request.user)

    def get_success_url(self, **kwargs):
        return reverse("index_user", args=[self.request.user.id])


def about(request):
    return render(request, "about.xhtml")
