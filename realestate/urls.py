from django.urls import path
from realestate.views import *

app_name = 'realestate'
urlpatterns = [
    # admin only links - property
    path('realestate/populate-property/', generate_property_page_numbers, name='property_admin_home'),
    path('realestate/populate-property/<int:segment>/', build_property_data, name='populate_property'),
    
    # admin only links - property address
    path('realestate/populate-property-address/', generate_property_address_page_numbers, name='property_address_admin_home'),
    path('realestate/populate-property-address/<int:segment>/', build_property_address_data, name='populate_property_address'),
    
    # admin only links - building
    path('realestate/populate-building/', generate_building_page_numbers, name='building_admin_home'),
    path('realestate/populate-building/<int:segment>/', build_building_data, name='populate_building'),
    
    # admin only links - building address
    path('realestate/populate-building-address/', generate_building_address_page_numbers, name='building_address_admin_home'),
    path('realestate/populate-building-address/<int:segment>/', build_building_address_data, name='populate_building_address'),
    
    # property links
    path('realestate/property/<int:property_id>/json/', get_property_as_json, name='property_json'),
    path('realestate/property/<int:property_id>/xml/', get_property_as_xml, name='property_xml'),
    path('realestate/property/', get_property_page, name='property_page'),
    path('realestate/property/<int:page>/', get_property_page, name='property_page'),
    
    # property address links
    path('realestate/property-address/<int:property_id>/json/', get_property_address_as_json, name='property_json'),
    path('realestate/property-address/<int:property_id>/xml/', get_property_address_as_xml, name='property_xml'),
    path('realestate/property-address/', get_property_address_page, name="property_address_page"),
    path('realestate/property-address/<int:page>/', get_property_address_page, name="property_address_page"),
    
    # building links
    path('realestate/building/<int:building_id>/json/', get_building_as_json, name='building_json'),
    path('realestate/building/<int:building_id>/xml/', get_building_as_xml, name='building_xml'),
    path('realestate/building/', get_building_page, name='building_page'),
    path('realestate/building/<int:page>/', get_building_page, name='building_page'),
    
    # building address links
    path('realestate/building-address/<int:building_id>/json/', get_building_address_as_json, name='building_json'),
    path('realestate/building-address/<int:building_id>/xml/', get_building_address_as_xml, name='building_xml'),
    path('realestate/building-address/', get_building_address_page, name="building_address_page"),
    path('realestate/building-address/<int:page>/', get_building_address_page, name="building_address_page"),
]
