from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Tweet
from .forms import TweetForm
from authentication.forms import LoginForm
# Create your views here.


def index(request):
    tweets = Tweet.objects.all()
    return render(request, "index.html", {
        "heading": "Tweets",
        "tweets": tweets,
    })


def new_tweet(request):
    context = {}
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_item = Tweet.objects.create(
                content=data['content'],
                author=request.user
            )
            return HttpResponseRedirect(reverse("profile", args=[request.user]))
    form=TweetForm()   
    context.update({'message': "Submitted Successfully!!!!! YAY!"})
    form = TweetForm()
    context.update({'form': form})
    return render(
        request, 
        "add_tweet.html", 
        context
    )


    