from rest_framework import serializers
from django.contrib.auth import get_user_model
from user_blog import services as likes_services
from user_blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'body',
            'is_fan',
            'total_likes',
        )

    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)


User = get_user_model()


class FanSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
        )
