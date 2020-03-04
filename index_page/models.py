from django.db import models


class Portfolios (models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    contacts = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.FilePathField(path="static/img")
