from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class PostLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


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
    likes = GenericRelation(PostLike)

    @property
    def total_likes(self):
        return self.likes.count()


class Category(models.Model):
    name = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.OneToOneField('user_topics.Topic', on_delete=models.CASCADE, primary_key=False)


class Comment(models.Model):
    path = ArrayField(models.IntegerField())
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField('Comment')
    date = models.DateTimeField('Date comment', default=timezone.now)

    def __str__(self):
        return self.body[0:200]

    def get_offset(self):
        return 5 if len(self.path) - 1 > 5 else len(self.path) - 1

    def get_col(self):
        return 12 - 5 if len(self.path) - 1 > 5 else 12 - len(self.path) - 1
