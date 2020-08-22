from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from user_blog.models import Category, Post
from user_page.models import Knowledge
from user_topics.models import Topic


class CreateTopic(LoginRequiredMixin, CreateView):
    model, fields = Topic, '__all__'
    template_name = 'topics_creator.html'

    def get_form(self, **kwargs):
        form_class = self.get_form_class()
        form = form_class(**self.get_form_kwargs())
        form.fields['user_portfolio'].queryset = Knowledge.objects.filter(user=self.request.user)
        form.fields['user_portfolio'].label_from_instance = lambda obj: "%s" % obj.name
        # print(form['user_portfolio'], form.fields['user_portfolio'])  # Form Field and him BoundField
        return form

    def get_success_url(self, **kwargs):
        return reverse("project_index", args=self.kwargs.values())

    def form_valid(self, form):
        self.object = form.save()
        Category(name=form["title"].value(), user=self.request.user, topic=self.object).save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['knowledge'] = self.kwargs.get('knowledge')
        return context


class Topics(ListView):
    template_name = 'topics_index.html'

    def get_queryset(self):
        topics = Topic.objects.filter(user_portfolio__user__username=self.kwargs.get('username')) \
            .filter(user_portfolio__name=self.kwargs.get('knowledge'))

        count_articles_topic = [
            Post.objects.filter(categories__id=Category.objects.get(topic=topic).id).count()
            for topic in topics
        ]

        articles_in = [
            Post.objects.filter(categories__id=Category.objects.get(topic=topic).id)
            for topic in topics
        ]

        scale_interval = (max(count_articles_topic) / 3)
        quantity_display = [
            'linear-gradient(90deg, rgba(233, 66, 66, 1) 44%, rgba(255, 255, 255, 1) 100%)'
            if count < scale_interval else
            'linear-gradient(90deg, rgba(233,226,66,1) 44%, rgba(255,255,255,1) 100%)'
            if scale_interval < count < scale_interval * 2 else
            'linear-gradient(90deg, rgba(66,233,66,1) 44%, rgba(255,255,255,1) 100%)'
            for count in count_articles_topic
        ]

        topics = list(zip(topics, count_articles_topic, quantity_display, articles_in))  # unpacking the iterator for reuse in the template
        return topics

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.kwargs.get('username')
        context['knowledge'] = self.kwargs.get('knowledge')
        return context


class TopicDetail(DetailView):
    model = Topic
    template_name = 'topics_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.kwargs.get('username')
        context['knowledge'] = self.kwargs.get('knowledge')
        return context
