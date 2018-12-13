from django.conf.urls import url
from . import views

app_name = 'good'

urlpatterns = [
    # /good/
    url (r'^$',  views.index, name='index'),
    # /good/156
    url (r'^(?P<category_id>[0-9]+)/$', views.detail, name='detail'),
    # /good/156/favorite
    url (r'^(?P<category_id>[0-9]+)/favorite$', views.favorite, name='favorite'),
]
