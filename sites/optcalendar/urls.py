from django.conf.urls.defaults import patterns, include, url
from optcalendar import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='idx'),
)
