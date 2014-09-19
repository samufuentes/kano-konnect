# Create your views here.

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from serializers import areaSerializer, facilitySerializer
from models import Area, Facility


class areaListView(ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = areaSerializer
    filter_fields = ('area_type',)

class areaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = areaSerializer


class facilityListView(ListAPIView):
    queryset = Facility.objects.all()
    serializer_class = facilitySerializer
    filter_fields = ('facility_area__area_name', 'facility_area__id')


class facilitiesByLGAListView(ListAPIView):
    queryset = Facility.objects.filter(facility_area__area_type="LGA")
    serializer_class = facilitySerializer
    filter_fields = ('facility_area__area_name', 'facility_area__id')


class facilitiesByZoneListView(ListAPIView):
    queryset = Facility.objects.filter(facility_area__area_type="State Zone")
    serializer_class = facilitySerializer
    filter_fields = ('facility_area__area_name', 'facility_area__id')


class facilitiesByWardListView(ListAPIView):
    queryset = Facility.objects.filter(facility_area__area_type="Ward")
    serializer_class = facilitySerializer
    filter_fields = ('facility_area__area_name', 'facility_area__id')
