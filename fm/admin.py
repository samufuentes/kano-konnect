from django.contrib import admin
from fm.models import Area, Facility, Contact, Role

class AreaAdmin(admin.ModelAdmin):
    pass

class FacilityAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

class RoleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Area, AreaAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Role, RoleAdmin)