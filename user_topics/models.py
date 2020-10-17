from django.db import models
from user_blog.models import Category


class Topic(models.Model):
    #  Add validation for queryset <knowledge>
    knowledge = models.ForeignKey('user_page.Knowledge', on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=120)
    description = models.TextField()
