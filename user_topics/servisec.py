from django.db.models import Count

from user_blog.models import Post, Category
from user_topics.models import Topic


def get_extended_queryset_topic(view_obj):
    topics = Topic.objects.filter(knowledge__user__username=view_obj.kwargs.get('username')) \
        .filter(knowledge__name=view_obj.kwargs.get('knowledge')) \
        .annotate(count_likes=Count('category__posts__likes')).order_by('-count_likes')

    count_likes_articles_topic = [
        Post.objects.filter(categories__id=Category.objects.get(topic=topic).id)
            .aggregate(Count('likes'))['likes__count']
        for topic in topics
    ]

    articles_in = [
        Post.objects.filter(categories__id=Category.objects.get(topic=topic).id).order_by('-created_on')
        for topic in topics
    ]

    scale_interval = (max(count_likes_articles_topic) / 3) if len(count_likes_articles_topic) != 0 else 0
    quantity_display = [
        'linear-gradient(90deg, rgba(233, 66, 66, 1) 44%, rgba(255, 255, 255, 1) 100%)'
        if count < scale_interval else
        'linear-gradient(90deg, rgba(233,226,66,1) 44%, rgba(255,255,255,1) 100%)'
        if scale_interval < count < scale_interval * 2 else
        'linear-gradient(90deg, rgba(66,233,66,1) 44%, rgba(255,255,255,1) 100%)'
        for count in count_likes_articles_topic
    ]

    return list(zip(topics, count_likes_articles_topic, quantity_display,
                    articles_in))  # unpacking the iterator for reuse in the template
