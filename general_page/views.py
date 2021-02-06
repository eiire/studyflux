from django.views.generic import TemplateView


class GeneralPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(GeneralPage, self).get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context
