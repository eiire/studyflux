from django import template
import json

register = template.Library()


@register.filter(name='make_topic_names')
def _make_topic_names(obj):
    topics = []

    for topic in obj:
        topics.append(topic[0].title)

    return json.dumps(topics)


@register.filter(name='make_topic_likes')
def _make_topic_list(obj):
    topics_likes = []

    for topic in obj:
        topics_likes.append(topic[1])

    return json.dumps(topics_likes)


@register.filter(name='make_topic_colors')
def _make_topic_list(obj):
    topics_colors = []

    for topic in obj:
        topics_colors.append(topic[2])

    return json.dumps(topics_colors)
