"""secateur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("block/", views.Block.as_view(), name="block-accounts"),
    path("search/", views.Search.as_view(), name="search"),
    path("log-messages/", views.LogMessages.as_view(), name="log-messages"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("disconnect/", views.Disconnect.as_view(), name="disconnect"),
    path("disconnected/", views.Disconnected.as_view(), name="disconnected"),
    url("", include("social_django.urls", namespace="social")),
]
