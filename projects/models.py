from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    technology = models.CharField(max_length=30)
    image = models.FilePathField(path="static/img")
    github = models.CharField(max_length=100)
    name_for_portfolios = models.CharField(max_length=100)
