from django.db import models
from django.contrib.auth.models import User


class Confirm(models.Model):
    token = models.CharField(max_length=100)
    code = models.CharField(max_length=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
