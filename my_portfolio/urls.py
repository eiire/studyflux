from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user_page import views

urlpatterns = [
    path("", views.StartPageView.as_view(), name='TEST'),

    path('users/@<username>/', include('user_page.urls'), {}),
    path('users/@<username>/', include('user_topics.urls')),
    path('users/@<username>/blog/', include('user_blog.urls')),

    path('ckeditor', include('ckeditor_uploader.urls')),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),

    path('like_api/v1/', include('apis.like_api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
