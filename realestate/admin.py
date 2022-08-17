from django.contrib import admin
from realestate.models import Property, Building, PropertyAddress

admin.site.register(Property)
admin.site.register(Building)
admin.site.register(PropertyAddress)
