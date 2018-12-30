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

    # /listing/category/add
    url (r'category/add/$', views.CategoryCreate.as_view(), name='category-add'),

    # /listing/category/2
    url (r'category/(?P<pk>[0-9]+)/$', views.CategoryUpdate.as_view(), name='category-update'),
    # /listing/category/2/delete
    url (r'category/(?P<pk>[0-9]+)/delete$', views.CategoryDelete.as_view(), name='category-delete'),
]
