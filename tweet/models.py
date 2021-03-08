from django.db import models
from django.utils import timezone
from twitterclone import settings
# Create your models here.

class Tweet(models.Model):
    content = models.TextField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

  