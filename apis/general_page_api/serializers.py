from rest_framework import serializers

from apis.general_page_api import services
from apis.like_api import services as likes_services
from user_blog.models import Post
from user_topics.models import Topic


class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    knowledge_field = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'image',
            'knowledge_field',
            'is_fan',
            'total_likes',
            'categories',
            'header',
            'body',
            'created_on',
            'last_modified',
        )

    def get_categories(self, obj):
        topics = services.get_topics(obj)
        serializer = TopicSerializer(topics, many=True)
        return serializer.data

    def get_knowledge_field(self, obj):
        knowledge = services.get_knowledge_name(obj)
        return knowledge

    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)


class TopicSerializer(serializers.ModelSerializer):
    knowledge = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = (
            'id',
            'knowledge',
            'title',
            'description',
        )

    def get_knowledge(self, obj):
        knowledge = services.get_knowledge_name(obj)
        return knowledge
