from django.conf.urls import patterns, url

from views import areaListView, areaDetailView, facilityListView, facilitiesByLGAListView,\
    facilitiesByWardListView, facilitiesByZoneListView, contactsByLGAListView, contactsByZoneListView, \
    contactsByWardListView



urlpatterns = patterns('',
    url(r'^facilities/$', facilityListView.as_view(), name='facility-list'),
    url(r'^facilities/lga/$', facilitiesByLGAListView.as_view(), name='lga-facility-list'),
    url(r'^facilities/zone/$', facilitiesByZoneListView.as_view(), name='zone-facility-list'),
    url(r'^facilities/ward/$', facilitiesByWardListView.as_view(), name='ward-facility-list'),
    url(r'^area/$', areaListView.as_view(), name='area-list'),
    url(r'^area_detail/(?P<pk>[0-9]+)/$', areaDetailView.as_view(), name='area-detail'),
    url(r'^contacts/lga/$', contactsByLGAListView.as_view(), name='lga-contacts-list'),
    url(r'^contacts/zone/$', contactsByZoneListView.as_view(), name='zone-contacts-list'),
    url(r'^contacts/ward/$', contactsByWardListView.as_view(), name='ward-contacts-list'),
)
