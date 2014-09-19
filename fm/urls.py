from django.conf.urls import patterns, url

from views import areaListView, areaDetailView, facilityListView, facilitiesByLGAListView, facilitiesByWardListView, facilitiesByZoneListView


urlpatterns = patterns('',
    url(r'^facilities/$', facilityListView.as_view(), name='facility-list'),
    url(r'^lga/$', facilitiesByLGAListView.as_view(), name='lga-facility-list'),
    url(r'^zone/$', facilitiesByZoneListView.as_view(), name='zone-facility-list'),
    url(r'^ward/$', facilitiesByWardListView.as_view(), name='ward-facility-list'),
    url(r'^area/$', areaListView.as_view(), name='area-list'),
    url(r'^area_detail/(?P<pk>[0-9]+)/$', areaDetailView.as_view(), name='area-detail'),

)
