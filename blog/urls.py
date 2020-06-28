from django.urls import path
from . import views

urlpatterns = [
    path("@<user_id>/", views.ListArticles.as_view(), name="article_index"),
    path("@<user_id>/create/", views.CreateArticleView.as_view(), name="article_creation"),
    path("@<user_id>/delete/<int:pk>/", views.DeleteArticleView.as_view(), name="article_dlt"),
    path("@<user_id>/<int:pk>/", views.DetailArticleView.as_view(), name="article_detail"),
    path("@<user_id>/<category_id>/posts/", views.TopicArticles.as_view(), name="article_category"),
    path("@<user_id>/edit_article/<int:pk>", views.UpdateArticleView.as_view(), name="update_article")
]
