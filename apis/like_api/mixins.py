from rest_framework.decorators import action
from rest_framework.response import Response
from . import services
from .serializers import FanSerializer


class LikedMixin:
    @action(methods=['POST'], url_path='like', detail=True)
    def post_like(self, request, pk=None):
        obj = self.get_object()
        services.to_like(obj, request.user)
        return Response()

    @action(methods=['POST'], url_path='unlike', detail=True)
    def post_unlike(self, request, pk=None):
        obj = self.get_object()
        services.to_unlike(obj, request.user)
        return Response()

    @action(methods=['GET'], url_path='fans', detail=True)
    def get_fans(self, request, pk=None):
        """Gets all users who like ʻobj`."""
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)
