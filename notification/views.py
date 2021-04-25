from django.shortcuts import render
from notification.models import Notification
from tweet.models import Tweet
from twitteruser.models import TwitterUser
import re
# Create your views here.
def notification_view(request):
    notifications = Notification.objects.filter(user_notify=request.user, seen=False).order_by('-id')
    for notification in notifications:
        notification.seen = True
        notification.save()
    return render(request, 'notification.html', {
        'notifications': notifications,
    })

def notification_new(user, tweet):
    # creating new notifications for following  users
    followuser = user.follow_users.all()
    for follower in followuser:
        Notification.objects.create(
            tweet_notify=tweet,
            user_notify=follower
            )
    # creating new notifications by tweet mentions
    notification_mentions(tweet)

def notification_mentions(tweet):
    tweet_content = tweet.content
    # filtering just words beginning w/ @
    mentions = re.findall(r'(^|\s)(@\w+)', tweet_content)
    for mention in mentions:
        mentionuser = mention[1]
        # removing @ from username
        mentionuser = mentionuser[1:]
        # checking if the user exists
        twitteruser = TwitterUser.objects.filter(username=mentionuser)
        if twitteruser.count() > 0:
            # if exists send a notification
            Notification.objects.create(
                tweet_notify=tweet,
                user_notify=twitteruser.get()
            )


    

