from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url (r'^$',  views.index, name='index'),
    # /good/156
    url (r'^(?P<category_id>[0-9]+)/$', views.detail, name='detail')
]
