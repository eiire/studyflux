from django.shortcuts import render
from index_page.models import Portfolios

# Create your views here.
def index(request):
    portfolios = Portfolios.objects.all()
    context = {
        'portfolios': portfolios
    }
    return render(request, "index.xhtml", context)


def about(request):
    return render(request, "about.xhtml")
