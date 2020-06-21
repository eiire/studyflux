from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Portfolios (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=30)
    topics = models.IntegerField(default=0)
    image = models.ImageField(upload_to='portfolio')