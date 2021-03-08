from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required
from .models import TwitterUser, UserFollowing
from django.contrib.auth.models import User
# Create your views here.



@login_required
def Profile(request):
    tweets = Tweet.objects.all()
    if User.is_authenticated:
        return render(request, 'profile.html', {
            'tweets': tweets
    })
    else:
        return HttpRedirect('login')




def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':   
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'account/register.html', context)
