from django.shortcuts import render
from projects.models import Project


def project_index(request, name_portfolio):
    projects = Project.objects.filter(name_for_portfolios=name_portfolio)
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
