from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.get_startpage, name="index"),
    path("about/", views.about, name="about"),
    path("login/", auth_views.LoginView.as_view(), name="index_auth"),
    path("<int:user_portfolios>/", views.get_userpage, name="get_userpage"),
    # path("<int:user_portfolios>/<name_portfolio>/", views.XXX, name="XXX")
]