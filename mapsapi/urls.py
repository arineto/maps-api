from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^filter/(?P<color>\w+)/$', 'core.views.home', name='home'),
    url(r'^new_map/$', 'core.views.new_map', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
