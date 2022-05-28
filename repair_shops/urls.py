from django.urls import path
from repair_shops.views import build_automobile_data

app_name = 'repair_shop'
urlpatterns = [
    path('populate-repair-shop/<int:segment>/', build_automobile_data, name='populate_repair_shop'),
]
