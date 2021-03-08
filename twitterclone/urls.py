"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tweet.views import index, new_tweet
from authentication.views import loginPage, registerPage
from django.urls import path
from twitteruser.views import Profile
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('templates/', include('django.contrib.auth.urls')),
    path('profile/', Profile, name='profile'),
    path('register/', registerPage, name="register"),
    path('login/', admin.site.urls, name="login"),
    path('index/', index, name='index'),
    path('add/', new_tweet, name='new_tweet'),
    path('admin/', admin.site.urls),
]
