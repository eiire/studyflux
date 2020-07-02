from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="user_blog/art_cover", blank=True)
    knowledge_field = models.ForeignKey('user_page.Knowledge', on_delete=models.CASCADE, primary_key=False)
    categories = models.ManyToManyField('Category', related_name='posts', blank=True)
    header = models.TextField(max_length=1000, default="This article is very interesting! :)")
    body = RichTextUploadingField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.OneToOneField('user_topics.Topic', on_delete=models.CASCADE, primary_key=False)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=70)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
