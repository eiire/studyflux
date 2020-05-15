from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.get_startpage, name="index"),
    path("about/", views.about, name="about"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("@<user_portfolios>/", views.get_userpage, name="get_userpage"),
    path("test/", views.CreatePortfolio.as_view(), name="test"),

    # path("<int:user_portfolios>/<name_portfolio>/", views.XXX, name="XXX")
]
