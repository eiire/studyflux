from django.contrib import admin
from user_topics.models import Topic
# Register your models here.


class TopicsViews(admin.ModelAdmin):
    pass


admin.site.register(Topic, TopicsViews)

