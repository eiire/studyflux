from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apis.general_page_api.serializers import PostSerializer
from user_blog.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
