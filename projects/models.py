from django.db import models


class Project(models.Model):
    user_portfolio = models.ForeignKey('index_page.Portfolios', on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=120)
    description = models.TextField()
    technology = models.CharField(max_length=30)
    # other path for win
    # image = models.FilePathField(path="img")
    github = models.CharField(max_length=100)
    name_for_portfolios = models.CharField(max_length=100, default='Project')
