"""django_login URL Configuration

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
    1. Add an import:  from blog imposrt urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from loginapp.views import home_view, UserCreateView, UpdateProfileView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_view, name="home_view"),
    url(r'^update_profile/(?P<pk>\d+)/$', login_required(UpdateProfileView.as_view()), name="update_profile"),
    url(r'^create_account/$', UserCreateView.as_view(), name="create_account"),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
