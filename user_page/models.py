from django.db import models
from django.contrib.auth.models import User
from user_topics.models import Topic


class Knowledge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='portfolio')

    @property
    def topics(self):
        return Topic.objects.filter(user_portfolio=self).count()