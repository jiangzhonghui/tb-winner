from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simple_todo_site.views.home', name='home'),
    #url(r'^simple_todo_site/', include('simple_todo_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url('^$', 'views.index', name='idx'),
    url(r'^promo/', 'promo.views.index', name='promo'),
    url(r'^optcalendar/', 'optcalendar.views.index', name='optcalendar'),
    url(r'^optanalysis/', 'optanalysis.views.index', name='optanalysis'),
    url(r'^optcrm/', 'optcrm.views.index', name='optcrm'),
    url(r'^opthelper/', 'opthelper.views.index', name='opthelper'),
    url(r'^optlog/', 'optlog.views.index', name='optlog'),
    url(r'^socialsales/', 'socialsales.views.index', name='socialsales'),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
