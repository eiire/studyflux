from . import views
from django.urls import path


urlpatterns = [
    path("", views.UserPageView.as_view(), name="UserPage"),
    path("create/<slug:knowledge>/", views.CreateKnowledge.as_view(), name="CreateKnowledge"),
    path("delete/<int:pk>/", views.DeleteKnowledge.as_view(), name="portfolio_dlt"),
    path("about/", views.about, name="about"),
]
