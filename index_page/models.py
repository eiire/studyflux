from django.contrib.auth.models import User
from django.db import models


class Portfolios (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    contacts = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
