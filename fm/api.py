from tastypie.resources import ModelResource
from fm.models import Area, Facility, Contact, Role

class AreaResource(ModelResource):
    class Meta:
        queryset = Area.objects.all()

class FacilityResource(ModelResource):
    class Meta:
        queryset = Facility.objects.all()

class ContactResource(ModelResource):
    class Meta:
        queryset = Contact.objects.all()

class RoleResource(ModelResource):
    class Meta:
        queryset = Role.objects.all()