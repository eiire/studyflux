from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, ListView, DeleteView
from user_blog.models import Post
from user_page.models import Knowledge
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class StartPageView(ListView):
    def get(self, request, *args, **kwargs):
        return redirect('UserPage', 'CHANGE_USER')


class UserPageView(ListView):
    template_name = "user_page.html"
    context_object_name = 'knowledges'

    def get_queryset(self):
        return Knowledge.objects.filter(user__username=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user__username=self.kwargs.get('username'))  # [task] Pin posts
        context['username'] = self.kwargs.get('username')
        return context


class UserProfile():
    pass


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "registration_page.html"

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
        user_knowledge = [el['name'] for el in Knowledge.objects.filter(user=request.user.id).values('name')]

        if kwargs.get('knowledge') in all_knowledge and kwargs.get('knowledge') not in user_knowledge:
            Knowledge(user=request.user, name=kwargs['knowledge'], topics=0, image=knowledge_img[kwargs['knowledge']])\
                .save()

        return redirect('UserPage', self.request.user.username)


class DeleteKnowledge(DeleteView, LoginRequiredMixin):
    model = Knowledge
    template_name = 'knowledge_confirm_delete.html'

    def get_queryset(self):
        return Knowledge.objects.filter(user=self.request.user)

    def get_success_url(self, **kwargs):
        return reverse("UserPage", args=[self.request.user.id])


def about(request, username):
    context = {'username': username}
    return render(request, "personal_information.xhtml", context)
