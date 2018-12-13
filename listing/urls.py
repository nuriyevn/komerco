from django.conf.urls import url
from . import views

app_name = 'listing'

urlpatterns = [
    # /listing/
    url (r'^$',  views.index, name='index'),
    # /listing/156
    url  (r'^(?P<category_id>[0-9]+)/$', views.detail, name='detail'),
    # /listing/156/favorite
    url (r'^(?P<category_id>[0-9]+)/favorite$', views.favorite, name='favorite'),
]
