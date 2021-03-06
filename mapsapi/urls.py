from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^filter/(?P<color>\w+)/$', 'core.views.home', name='home'),
    url(r'^save_map/$', 'core.views.save_map', name='save_map'),
    url(r'^save_map/(?P<map_id>\d+)/$', 'core.views.save_map', name='save_map'),
    url(r'^delete_map/(?P<map_id>\d+)/$', 'core.views.delete_map', name='delete_map'),
    url(r'^edit_map/(?P<map_id>\d+)/$', 'core.views.edit_map', name='edit_map'),
    url(r'^add_quarry/(?P<map_id>\d+)/$', 'core.views.add_quarry', name='add_quarry'),
    url(r'^logout/$', 'core.views.logout_aux', name='logout_aux'),
    url(r'^login/$', 'core.views.login_aux', name='login_aux'),
    url(r'^admin/', include(admin.site.urls)),
)
