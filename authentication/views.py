from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, HttpResponseRedirect, reverse, render
from authentication.forms import LoginForm, AddUser
from twitteruser.models import TwitterUser



def registerPage(request):
    form = AddUser()
    if request.method == 'POST':
        form =AddUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
            )
            user.follow_users.add(user)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))  

    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("home")))

    form = LoginForm()
    return render(request, "login.html", {'form': form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
    