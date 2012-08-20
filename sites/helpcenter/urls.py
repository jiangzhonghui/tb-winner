from django.conf.urls.defaults import patterns, urls
from helpcenter import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='helpcenter'),
)
