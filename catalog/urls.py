from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^music$', views.MusicListView.as_view(), name='music'),
   # url(r'^music/(?P<pk>\d+)$', views.MusicDetailView.as_view(), name='music-detail'),
]
