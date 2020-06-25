from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from blog.forms import CommentForm, ModelFormPostMixin
from blog.models import Post, Comment

from django.contrib.auth.mixins import LoginRequiredMixin


class TopicArticles(ListView):
    template_name = 'article_category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(categories__name__contains=self.kwargs.get('category')).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super(TopicArticles, self).get_context_data(**kwargs)
        context['category'] = self.kwargs.get('category')
        context['current_user_id'] = self.request.user.pk
        context['user_id'] = self.kwargs.get('user_id')
        return context


class CreateArticleView(ModelFormPostMixin, CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'articles_readactor.html'


class UpdateArticleView(ModelFormPostMixin, UpdateView, LoginRequiredMixin):
    """ View initializes data from the model-object instance """
    model = Post
    template_name = 'articles_readactor.html'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)  # after get_object if <pk> in url


class DeleteArticleView(ModelFormPostMixin, DeleteView, LoginRequiredMixin):
    model = Post
    template_name = 'article_confirm_delete.html'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


class ListArticles(ListView):
    template_name = 'article_index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.kwargs.get('user_id')
        context['is_user'] = self.request.user.is_authenticated
        context['user'] = True if self.request.user.is_authenticated else False
        return context


class DetailArticleView(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        return context