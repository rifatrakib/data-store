from django.urls import path
from property_sales.views import build_property_sales_data

app_name = 'property_sales'
urlpatterns = [
    path('populate-sales-record/<int:segment>/', build_property_sales_data, name='populate_sales_record'),
]
