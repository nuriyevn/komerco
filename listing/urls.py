from django.conf.urls import url
from . import views

app_name = 'listing'

urlpatterns = [
    # /listing/
    url (r'^$',  views.IndexView.as_view(), name='index'),
    # /listing/156
    url  (r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /listing/156/favorite
    #url (r'^(?P<category_id>[0-9]+)/favorite$', views.favorite, name='favorite'),
    url (r'listing/add/$', views.CategoryCreate.as_view(), name='category-add'),

]
