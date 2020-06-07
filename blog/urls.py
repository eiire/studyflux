from django.urls import path
from . import views

urlpatterns = [
    path("@<user>/", views.article_index, name="article_index"),
    path("@<user_id>/create/", views.CreateArticle.as_view(), name="article_creation"),
    path("@<user_id>/delete/<int:pk>/", views.article_dlt, name="article_dlt"),
    path("@<user_id>/<int:pk>/", views.article_detail, name="article_detail"),
    # path("@<user_id>/edit/<user_id>/<int:pk>/", views.CreateArticle.as_view(), name="article_creation"),
    path("@<user_id>/<category>/posts/", views.article_category, name="article_category"),
]
