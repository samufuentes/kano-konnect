from django.conf.urls import patterns, url

from views import areaListView, areaDetailView, facilityListView

urlpatterns = patterns('',
    url(r'^facilities/$', facilityListView.as_view(), name='facility-list'),
    url(r'^area/$', areaListView.as_view(), name='area-list'),
    url(r'^area_detail/(?P<pk>[0-9]+)/$', areaDetailView.as_view(), name='area-detail'),

)
