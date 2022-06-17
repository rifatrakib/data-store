from django.urls import path
from property_sales.views import *

app_name = 'property_sales'
urlpatterns = [
    path('sales-record/sales/', get_property_sales_page, name='property_sales_page'),
    path('sales-record/sales/<int:page>/', get_property_sales_page, name='property_sales_page'),
    path('sales-record/<int:sales_id>/json/', get_property_sales_as_json, name='sales_record_json'),
    path('sales-record/<int:sales_id>/xml/', get_property_sales_as_xml, name='sales_record_xml'),
    path('populate-sales-record/', generate_page_numbers, name='property_sales_admin_home'),
    path('populate-sales-record/<int:segment>/', build_property_sales_data, name='populate_sales_record'),
]
