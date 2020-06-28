from django.db import models
from blog.models import Category


class Project(models.Model):
    #  Add validation for queryset <user_portfolio>
    user_portfolio = models.ForeignKey('index_page.Portfolios', on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=120)
    description = models.TextField()
