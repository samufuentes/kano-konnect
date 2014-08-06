from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from tastypie.api import Api
from fm.api import AreaResource, FacilityResource, ContactResource, RoleResource

import auto_deploy
import tastypie_swagger

from django.contrib import admin
admin.autodiscover()

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
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
