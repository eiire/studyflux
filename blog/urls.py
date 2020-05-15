from django.urls import path
from . import views

urlpatterns = [
    path("@<user>/create/", views.CreateArticle.as_view(), name="article_creation"),
    path("@<user>/", views.blog_index, name="article_index"),
    path("<int:pk>/", views.blog_detail, name="article_detail"),
    path("<category>/", views.blog_category, name="article_category"),
]
