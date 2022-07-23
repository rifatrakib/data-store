from django.urls import path
from realestate.views import *

app_name = 'realestate'
urlpatterns = [
    path('realestate/property/<int:property_id>/json/', get_property_as_json, name='property_json'),
    path('realestate/building/<int:building_id>/json/', get_building_as_json, name='building_json'),
]
