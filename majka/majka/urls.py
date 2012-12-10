from django.conf.urls import include, url, patterns
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

_patterns = (
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'majka.views.home'),
    # musi byc ostatnie jezeli puste
    url(r'^', include('bricks.urls')),
)

urlpatterns = patterns('', *_patterns)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
