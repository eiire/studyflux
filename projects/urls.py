from django.urls import path
from . import views

urlpatterns = [
    path("@<user_id>/create_in/<id_knowledge>", views.CreateTopic.as_view(), name='project_creator'),
    path("@<user_id>/<id_knowledge>/", views.Topics.as_view(), name="project_index"),
    path("@<user_id>/portfolio_<id_knowledge>/project_<pk>/", views.project_detail, name="project_detail"),
]