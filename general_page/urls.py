from django.urls import path
from general_page import views

urlpatterns = [
    path("", views.GeneralPage.as_view(), name='app'),
]
