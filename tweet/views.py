from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Tweet
from .forms import TweetForm
from authentication.forms import LoginForm
from django.contrib.auth.decorators import login_required
from notification.models import Notification
from notification.views import notification_new
import re
from twitteruser.models import TwitterUser
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

@login_required
def index(request):
    #filters stuff defining variables to call
    user = request.user
    followuser = user.follow_users.all()
    tweets = Tweet.objects.filter(author__in=followuser).order_by('-date_posted')
    notifications = Notification.objects.filter(user_notify=user, seen=False)
    return render(request, "index.html", {
        "heading": "Tweets",
        "tweets": tweets,
        "user": user,
        "notifications": notifications,
    })


def detail_tweet(request, id):
    tweet = Tweet.objects.filter(id=id).first()
    return render(request, 'tweetdetail.html', {'tweet': tweet})




def new_tweet(request):
    context = {}
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Adds a tweet
            new_item = Tweet.objects.create(
                content=data['content'],
                author=request.user
                )
            #Adds Notification :)
            notification_new(request.user, new_item)
            return HttpResponseRedirect(reverse("home"))        
    form=TweetForm()   
    context.update({'message': "Submitted Successfully!!!!! YAY!"})
    form = TweetForm()
    context.update({'form': form})
    return render(
        request,
        "add_tweet.html",
        context,
    )


    