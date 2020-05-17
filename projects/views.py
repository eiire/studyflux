from django.shortcuts import render
from projects.models import Project


def project_index(request, user_id, name_portfolio):

    projects = Project.objects.filter(user_portfolio=user_id)
    context = {
        'user_id': user_id,
        'user_auth': request.user.is_authenticated,
        'projects': projects,
        'name_portfolio': name_portfolio,
    }
    return render(request, 'project_index.html', context)


def project_detail(request, user_id, name_portfolio, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'user_id': user_id,
        'user_auth': request.user.is_authenticated,
        'name_portfolio': name_portfolio,
        'project': project,
    }
    return render(request, 'project_detail.html', context)
