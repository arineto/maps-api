from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^filter/(?P<color>\w+)/$', 'core.views.home', name='home'),
    url(r'^new_map/$', 'core.views.new_map', name='new_map'),
    url(r'^delete_map/(?P<map_id>\d+)/$', 'core.views.delete_map', name='delete_map'),
    url(r'^admin/', include(admin.site.urls)),
)
