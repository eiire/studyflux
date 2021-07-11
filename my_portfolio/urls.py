import ckeditor_uploader
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib.auth import views as auth_views
from ckeditor_uploader import views
from django.views.decorators.cache import never_cache
from my_portfolio.view import CustomDjangoLoginView
from user_page import views
from apis.auth_api.view import signup, signin, check_auth, _logout
from apis.general_page_api.view import get_user
from my_portfolio.batteries_patches.ckeditor_uploader_patch import upload

urlpatterns = [
    # path("", views.StartPageView.as_view(), name='TEST'),
    path("", include('general_page.urls')),
    # path("", include('user_page.urls')),

    path('users/@<username>/', include('user_page.urls'), {}),
    path('users/@<username>/', include('user_topics.urls')),
    path('users/@<username>/blog/', include('user_blog.urls')),

    # path('ckeditor', include('ckeditor_uploader.urls')), default staff_member_required
    path('upload/', login_required(upload), name='ckeditor_upload'),
    # browse files from the server for is_staff users
    path('browse/', never_cache(staff_member_required(ckeditor_uploader.views.browse)), name='ckeditor_browse'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('register123/', signup, name='register123'),
    # path('login/', CustomDjangoLoginView.as_view(), name='login'),
    path('login/', signin, name='login'),
    path('check_auth/', check_auth, name='check_auth'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout_api/', _logout, name='logout_api'),
    path('admin/', admin.site.urls),

    path('general_page_api/v1/', include('apis.general_page_api.urls')),
    path('like_api/v1/', include('apis.like_api.urls')),
    path('get-user/', get_user, name='register123'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
