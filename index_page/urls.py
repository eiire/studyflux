from . import views
from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


urlpatterns = [
    path("", views.get_startpage, name="index"),
    path("about/", views.about, name="about"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterFormView.as_view(), name="register"),
    path("@<user_id>/", views.get_userpage, name="get_userpage"),
    path("@<user_id>/create/", views.CreatePortfolio.as_view(), name="create_portfolio"),
    # path("<int:user_portfolios>/<name_portfolio>/", views.XXX, name="XXX")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
