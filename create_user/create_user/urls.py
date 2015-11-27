"""create_user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from create.views import UserCreateView, indexview, RedirectView, StudentView, TeacherView, ProfileUpdate
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', indexview),
    url(r'^redirect/$', RedirectView.as_view(), name='redirect'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^create_user/', UserCreateView.as_view(), name='user_create'),
    url(r'^teacher/$', TeacherView.as_view(), name='teacher'),
    url(r'^student/$', StudentView.as_view(), name='student'),
    url(r'^update_profile/(?P<pk>\d+)/$', login_required(ProfileUpdate.as_view()), name='profile_update'),
    url(r'^admin/', include(admin.site.urls)),
]
