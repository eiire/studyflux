from . import views
from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


urlpatterns = [
    path("", views.StartPageView.as_view(), name="index"),
    path("@<int:user_id>/", views.UserPageView.as_view(), name="index_user"),
    path("@<int:user_id>/create/<slug:knowledge>", views.CreateKnowledge.as_view(), name="create_portfolio"),
    path("@<int:user_id>/delete/<int:pk>/", views.DeleteKnowledge.as_view(), name="portfolio_dlt"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterFormView.as_view(), name="register"),
    path("about/", views.about, name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
