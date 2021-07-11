from django.urls import path
from general_page import views

urlpatterns = [
    path("", views.GeneralPage.as_view(), name='app'),
    path("signup", views.GeneralPage.as_view(), name='signup'),
    path("signin", views.GeneralPage.as_view(), name='signin'),
    path("profile", views.GeneralPage.as_view(), name='profile'),
]
