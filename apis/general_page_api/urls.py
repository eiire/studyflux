from rest_framework.routers import DefaultRouter

from apis.general_page_api.viewsets import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
urlpatterns = router.urls
