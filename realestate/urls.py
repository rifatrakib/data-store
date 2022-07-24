from django.urls import path
from realestate.views import *

app_name = 'realestate'
urlpatterns = [
    # property links
    path('realestate/property/<int:property_id>/json/', get_property_as_json, name='property_json'),
    path('realestate/property/<int:property_id>/xml/', get_property_as_xml, name='property_xml'),
    
    # building links
    path('realestate/building/<int:building_id>/json/', get_building_as_json, name='building_json'),
    path('realestate/building/<int:building_id>/xml/', get_building_as_xml, name='building_xml'),
]
