from django.urls import path
from repair_shops.views import *

app_name = 'repair_shop'
urlpatterns = [
    path('repair-shop/shops/', get_repair_shop_page, name='repair_shop_page'),
    path('repair-shop/shops/<int:page>/', get_repair_shop_page, name='repair_shop_page'),
    path('repair-shop/<int:shop_id>/json/', get_repair_shops_as_json, name='repair_shop_json'),
    path('repair-shop/<int:shop_id>/xml/', get_repair_shops_as_xml, name='repair_shop_xml'),
    path('populate-repair-shop/', generate_page_numbers, name='repair_shop_admin_home'),
    path('populate-repair-shop/<int:segment>/', build_automobile_data, name='populate_repair_shop'),
]
