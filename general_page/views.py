from django.views.generic import TemplateView


class GeneralPage(TemplateView):
    template_name = 'index.html'
