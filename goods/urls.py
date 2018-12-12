from django.conf.urls import url
from . import views

urlpatterns = [
    url (r'^$',  views.index, name='index'),
    # /goods/156
    url (r'^(?P<category_id>[0-9]+)/$', views.detail, name='detail')
]
