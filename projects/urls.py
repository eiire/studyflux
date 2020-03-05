from django.urls import path
from . import views

urlpatterns = [
    path("<name_portfolio>", views.project_index, name="project_index"),
    path("<pk>/", views.project_detail, name="project_detail"),
]