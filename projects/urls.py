from django.urls import path
from . import views

urlpatterns = [
    path("@<user_id>/<name_portfolio>/", views.project_index, name="project_index"),
    path("@<user_id>/portfolio_<name_portfolio>/project_<pk>/", views.project_detail, name="project_detail"),
]