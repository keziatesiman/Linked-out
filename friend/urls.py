from django.conf.urls import url
from .views import index, add_friend

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_friend', add_friend, name='add_friend'),
 ]
