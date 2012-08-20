from django.conf.urls import patterns, include, url
from ui import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='uiidx'),
    url(r'^basecss/$', views.basecss, name='basecss'),
    url(r'^bootstrapexamples/$', views.bootstrapexamples, name='bootstrapexamples'),
    url(r'^button/$', views.button, name='button'),
    url(r'^compontents/$', views.compontents, name='compontents'),
    url(r'^customize/$', views.customize, name='customize'),
    url(r'^javascript/$', views.javascript, name='javascript'),
    url(r'^less/$', views.less, name='less'),
    url(r'^scaffolding/$', views.scaffolding, name='scaffolding'),
    url(r'^upgradebootstrap2/$', views.upgradebootstrap2, name='upgradebootstrap2'),
)
