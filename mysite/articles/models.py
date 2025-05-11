from django.contrib.auth.models import User
from django.db import models

from django.conf import settings


class Article(models.Model):
    title   = models.CharField(max_length=200)
    slug    = models.SlugField(unique=True)
    body    = models.TextField()
    date    = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="images/", blank=True, default='images/default.jpg')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[0:50] + '...'
