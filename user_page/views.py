from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, ListView, DeleteView
from user_blog.models import Post
from user_page.models import Knowledge
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class UserPageView(ListView):
    template_name = "user_page.html"
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(user__username=self.kwargs.get('username'), pinned=True) \
            .annotate(count=Count('likes')).order_by('-count')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['knowledges'] = Knowledge.objects.filter(user__username=self.kwargs.get('username'))
        context['username'] = self.kwargs.get('username')
        return context


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
            'All-streams': 'portfolio/2.png',
            'Development': 'portfolio/2.png',
            'Economics': 'portfolio/2.png',
            'Lifestyle': 'portfolio/2.png',
        }
        all_knowledge = ['All-streams', 'Development', 'Economics', 'Lifestyle']
        user_knowledge = [el['name'] for el in Knowledge.objects.filter(user=request.user.id).values('name')]

        if kwargs.get('knowledge') in all_knowledge and kwargs.get('knowledge') not in user_knowledge:
            Knowledge(user=request.user, name=kwargs['knowledge'], image=knowledge_img[kwargs['knowledge']])\
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
