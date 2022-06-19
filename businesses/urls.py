from django.urls import path
from businesses.views import *

app_name = 'businesses'
urlpatterns = [
    path('business-record/small-business/', get_small_business_page, name='small_business_page'),
    path('business-record/small-business/<int:page>/', get_small_business_page, name='small_business_page'),
    path('business-record/<int:business_id>/json/', get_small_business_as_json, name='business_record_json'),
    path('business-record/<int:business_id>/xml/', get_repair_shops_as_xml, name='business_record_xml'),
    path('populate-business-record/', generate_page_numbers, name='business_admin_home'),
    path('populate-business-record/<int:segment>/', build_small_business_data, name='populate_business_record'),
]
