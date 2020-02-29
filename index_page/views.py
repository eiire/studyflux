from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.xhtml", {})


def about(request):
    about = "about.xhtml"
    context = {
        'about': about
    }
    return render(request, "about.xhtml", context)
