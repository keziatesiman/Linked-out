from django.conf.urls import url
from .views import index, add_status, delete_status

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_status', add_status, name='add_status'),
    url(r'^delete/(?P<pk>\d+)/$', delete_status, name='delete_status')
]