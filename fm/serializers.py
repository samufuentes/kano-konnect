from models import Facility, Area, Contact
from rest_framework import serializers


class areaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = ('area_name', 'area_type', 'area_parent')


class facilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Facility
        fields = ('facility_name', 'facility_type', 'facility_status', 'facility_area',)
        exclude = ('json',)


class contactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('contact_name', 'contact_phone', 'contact_email', 'contact_area',)
        exclude = ('json',)