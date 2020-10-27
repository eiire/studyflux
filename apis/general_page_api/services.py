from user_blog.models import Post
from user_page.models import Knowledge
from user_topics.models import Topic


def get_topics(post):
    return Topic.objects.filter(category__posts=post)


def get_knowledge_name(obj):
    if type(obj) is Post:
        return Knowledge.objects.get(post=obj).name
    elif type(obj) is Topic:
        return Knowledge.objects.get(topic=obj).name
