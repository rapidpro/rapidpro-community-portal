from django.contrib import admin
from .models import Country, FocusArea, Organization, Service, Expertise

# Register your models here.
admin.site.register(Country)
admin.site.register(FocusArea)
admin.site.register(Organization)
admin.site.register(Service)
admin.site.register(Expertise)