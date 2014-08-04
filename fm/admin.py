from django.contrib import admin
from fm.models import Area, Facility, FacilityImage, Contact, Role

class AreaAdmin(admin.ModelAdmin):
    pass

class FacilityImageInline(admin.TabularInline):
    model = FacilityImage

class FacilityAdmin(admin.ModelAdmin):
    list_display = ('facility_name', 'facility_type', 'facility_status', 'facility_area')
    inlines = [FacilityImageInline]

class ContactAdmin(admin.ModelAdmin):
    pass

class RoleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Area, AreaAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Role, RoleAdmin)