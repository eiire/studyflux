from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("@<user>/", views.article_index, name="article_index"),
    path("@<user_id>/create/", views.CreateArticle.as_view(), name="article_creation"),
    path("@<user_id>/<int:pk>/", views.article_detail, name="article_detail"),
    path("<category>/", views.article_category, name="article_category"),
]
