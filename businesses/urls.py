from django.urls import path
from businesses.views import *

app_name = 'businesses'
urlpatterns = [
    path('populate-business-record/', generate_page_numbers, name='business_admin_home'),
    path('populate-business-record/<int:segment>/', build_small_business_data, name='populate_business_record'),
]
