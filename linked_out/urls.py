"""linked_out URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import user_profile.urls as user_profile
import dashboard.urls as dashboard
import status.urls as status
import friend.urls as friend
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(
        url='/dashboard/', permanent=True),
        name='index'),
    url(r'^user_profile/', include(user_profile, namespace="user_profile")),
    url(r'^dashboard/', include(dashboard, namespace="dashboard")),
    url(r'^status/', include(status, namespace="status")),
    url(r'^friend/', include(friend, namespace="friend")),
]
