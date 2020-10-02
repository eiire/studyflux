from django.http import JsonResponse
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView
from user_blog.forms import CommentForm, ModelFormPostMixin
from user_blog.models import Post, PostLike, Comment
from django.contrib.auth.mixins import LoginRequiredMixin


class TopicArticles(ListView):
    template_name = 'article_category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return list(dict.fromkeys(
            Post.objects.filter(user__username=self.kwargs.get('username')) \
                .filter(categories__name=self.kwargs.get('topic')).order_by('-created_on'))
        )  # __contains distinct

    def get_context_data(self, **kwargs):
        context = super(TopicArticles, self).get_context_data(**kwargs)
        context['username'] = self.kwargs.get('username')
        context['knowledge'] = self.kwargs.get('knowledge')
        return context


class CreateArticleView(ModelFormPostMixin, CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'articles_redactor.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        # A form based on the model(post) and does not exist field.user  in the form from request POST, bc commit=False.
        post = form.save(commit=False)
        post.user = self.request.user
        self.object = post
        return super().form_valid(form)


class UpdateArticleView(ModelFormPostMixin, UpdateView, LoginRequiredMixin):
    """ View initializes data from the model-object instance """
    model = Post
    template_name = 'articles_redactor.html'

    def get_queryset(self):
        return Post.objects.filter(user__username=self.request.user)  # after get_object if <pk> in url


class DeleteArticleView(ModelFormPostMixin, DeleteView, LoginRequiredMixin):
    model = Post
    template_name = 'article_confirm_delete.html'

    def get_queryset(self):
        return Post.objects.filter(user__username=self.request.user)


class ListArticles(ListView):
    template_name = 'article_index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(user__username=self.kwargs.get('username')).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.kwargs.get('username')
        return context


class DetailArticleView(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.kwargs.get('username')
        context['comments'] = Comment.objects.filter(post=self.object)
        return context


class LikeHandlerView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        if self.request.GET.get('rel') == 'Unliked':
            PostLike(user_id=self.request.user.id, post_id=self.request.GET.get('post_id')).save()
            print(Post.objects.get(postlike__post_id=self.request.GET.get('post_id')))
            return JsonResponse(data={'data': 'Liked', 'post_id': self.request.GET.get('post_id')})
        else:
            print(Post.objects.get(postlike__post_id=self.request.GET.get('post_id')), 'ff')
            # print(Post.objects.get(id__=self.request.GET.get('post_id')))
            PostLike.objects.filter(user_id=self.request.user.id, post_id=self.request.GET.get('post_id')).delete()
            return JsonResponse(data={'data': 'Unliked', 'post_id': self.request.GET.get('post_id')})
