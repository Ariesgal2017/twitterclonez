from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.forms import UserCreationForm
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required
from .models import TwitterUser
from django.contrib.auth.models import User
# Create your views here.

def follow(request, username):
    follower = TwitterUser.objects.get(username=username)
    currentUser = TwitterUser.objects.get(username=request.user.username)
    currentUser.follow_users.add(follower)
    currentUser.save()
    return redirect('home')

def unFollow(request, username):
    follower = TwitterUser.objects.get(username=username)
    currentUser = TwitterUser.objects.get(username=request.user.username)
    currentUser.follow_users.remove(follower)
    currentUser.save()
    return redirect('home')

@login_required
def Profile(request, username):
    tweets = Tweet.objects.all()
    follower = TwitterUser.objects.get(username=username)
    # tweets = TwitterUser.objects.get(u)
    return render(request, 'profile.html', {
        'tweets': tweets,
        'follower': follower,  
    })
    return HttpResponseRedirect(reverse('profile', args=[user.username]), {'tweet':tweet})


def userProfile(request, username):
    tweet = Tweet.objects.all()
    tweets = TwitterUser.objects.get(username=username)
    tweet_obj = Tweet.objects.filter(author=tweets).order_by('-date_posted')
    users = tweets.follow_users.all()
    return render(request, 'profile.html', {
        'tweet': tweets,
        'tweet_obj': tweet_obj,
        'users': users,
    })
    return HttpResponseRedirect(reverse('profile'), {'tweets':tweets})




def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':   
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'account/register.html', context)
