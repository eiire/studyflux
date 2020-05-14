from django.db import models
from index_page.models import Portfolios


class Project(models.Model):
    user_portfolio = models.ForeignKey(Portfolios, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=120)
    description = models.TextField()
    technology = models.CharField(max_length=30)
    # other path for win
    image = models.CharField(max_length=1000)
    github = models.CharField(max_length=100)
    name_for_portfolios = models.CharField(max_length=100, default='Portfolio')
