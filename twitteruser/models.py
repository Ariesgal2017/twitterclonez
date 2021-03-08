from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class TwitterUser(AbstractUser):
    display_name = models.CharField(max_length=180)
    follow_users = models.ManyToManyField("self", symmetrical=False)

class UserFollowing(models.Model):
    user_id = models.ForeignKey("TwitterUser", related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey("TwitterUser", related_name="followers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)