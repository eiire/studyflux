from django.contrib.auth.models import User
from django.db import models
from user_blog.models import Category


class Topic(models.Model):
    #  Add validation for queryset <knowledge>
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    knowledge = models.ForeignKey('user_page.Knowledge', on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=120)
    description = models.TextField()
