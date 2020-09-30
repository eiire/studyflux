from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListArticles.as_view(), name='article_index'),
    path('create/', views.CreateArticleView.as_view(), name='article_creation'),
    path('delete/<int:pk>/', views.DeleteArticleView.as_view(), name='article_dlt'),
    path('post/<int:pk>/', views.DetailArticleView.as_view(), name='article_detail'),
    path('flows/<knowledge>/topic/<topic>/posts/', views.TopicArticles.as_view(), name='article_category'),
    path('edit_article/<int:pk>', views.UpdateArticleView.as_view(), name='update_article'),
    path('ajax/', views.LikeHandlerView.as_view(), name='like_handler'),
    # path('likes/', views.LikeProcessingView.as_view(), name='like_proc'),
]
