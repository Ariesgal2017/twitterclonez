from django.db import models
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from django.utils import timezone

# Got help from Detrich Schilling in study hall.
# Create your models here.
class Notification(models.Model):
    seen = models.BooleanField(default=False)
    tweet_notify = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user_notify = models.ForeignKey(TwitterUser, related_name='usernotify', on_delete=models.CASCADE)

    
    def __str__(self):
        return (self.tweet_notify.content)


