from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from fm.models import Area, Facility, FacilityImage, Contact, Role

class AreaAdmin(SimpleHistoryAdmin):
    pass

class FacilityImageInline(admin.TabularInline):
    model = FacilityImage

class FacilityAdmin(SimpleHistoryAdmin):
    list_display = ('facility_name', 'facility_type', 'facility_status', 'facility_area')
    inlines = [FacilityImageInline]

class ContactAdmin(SimpleHistoryAdmin):
    pass

class RoleAdmin(SimpleHistoryAdmin):
    pass

admin.site.register(Area, AreaAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Role, RoleAdmin)