from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from tastypie.api import Api
from fm.api import AreaResource, FacilityResource, ContactResource, RoleResource
from fm.models import Area, Facility, Contact, Role
from django.contrib.auth.models import User

import auto_deploy
import tastypie_swagger

from django.contrib import admin
admin.autodiscover()

from rest_framework import viewsets, routers

# ViewSets define the view behavior.
class AreaViewSet(viewsets.ModelViewSet):
    model = Area

class FacilityViewSet(viewsets.ModelViewSet):
    model = Facility

class ContactViewSet(viewsets.ModelViewSet):
    model = Contact

class RoleViewSet(viewsets.ModelViewSet):
    model = Role

class UserViewSet(viewsets.ModelViewSet):
    model = User


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'areas', AreaViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'users', UserViewSet)


v1_api = Api(api_name='v1')
v1_api.register(AreaResource())
v1_api.register(FacilityResource())
v1_api.register(ContactResource())
v1_api.register(RoleResource())

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'kano_konnect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url( r'^autodeploy/', include('auto_deploy.urls', namespace='auto_deploy')),
    url(r'api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/', include(router.urls)),
    url(r'^rest-auth/', include('rest_framework.urls', namespace='rest_framework'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
