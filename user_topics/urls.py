from django.urls import path
from . import views

urlpatterns = [
    path('flows/<knowledge>/topics/create/', views.CreateTopic.as_view(), name='project_creator'),
    path('flows/<knowledge>/topics/', views.Topics.as_view(), name="project_index"),
    path('flows/<knowledge>/topic/<pk>/', views.TopicDetail.as_view(), name='project_detail'),
]