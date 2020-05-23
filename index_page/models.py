from django.db import models
from django.contrib.auth.models import User


class Portfolios (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=30)
    count_proj = models.IntegerField()
    contacts = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio')
