from django.urls import path
from property_sales.views import build_property_sales_data, generate_page_numbers

app_name = 'property_sales'
urlpatterns = [
    path('populate-sales-record/', generate_page_numbers, name='property_sales_admin_home'),
    path('populate-sales-record/<int:segment>/', build_property_sales_data, name='populate_sales_record'),
]
