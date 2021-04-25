from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, HttpResponseRedirect, reverse, render
from authentication.forms import LoginForm



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
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
