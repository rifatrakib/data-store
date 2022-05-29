import os
import json
from datetime import datetime
from django.shortcuts import render
from django.core import serializers
from core.decorators import admin_only
from django.contrib.gis.geos import Point
from core.utils import process_automobile_data
from django.http import HttpResponse, JsonResponse
from repair_shops.models import AutomobileRepairShop


@admin_only
def generate_page_numbers(request):
    file_names = os.listdir('raw-data/csv/automobile/')
    page_count = list(range(1, len(file_names) + 1))
    return render(request, 'repair_shops/index.html', {'page_count': page_count})


@admin_only
def build_automobile_data(request, segment):
    shops = process_automobile_data(segment)
    for shop in shops:
        geo_type = shop.get('geo_type', None)
        lon = shop.get('lon', None)
        lat = shop.get('lat', None)
        point_data = Point(lon, lat) if geo_type else None
        AutomobileRepairShop.objects.create(
            shop_number=shop.get('shop_number', None),
            business_name=shop.get('business_name', None),
            business_address=shop.get('business_address', None),
            city=shop.get('city', None),
            state=shop.get('state', None),
            zip_code=shop.get('zip_code', None),
            license_num=shop.get('license_num', None),
            license_type=shop.get('license_type', None),
            license_expiration=shop.get('license_expiration', None),
            location=point_data,
        )
    return render(request, 'repair_shops/shop-adminer.html')


def get_repair_shops_as_json(request, shop_id):
    shop_record = AutomobileRepairShop.objects.filter(pk=shop_id)
    data = json.loads(serializers.serialize('geojson', shop_record))
    response = {
        'source': request.build_absolute_uri(),
        'headers': dict(request.headers),
        'api': 'public',
        'identifier': shop_id,
        'success': True,
        'data': data,
        'format': 'text/json',
        'timestamp': str(datetime.utcnow()) + ' UTC',
    }
    return JsonResponse(response)


def get_repair_shops_as_xml(request, shop_id):
    shop_record = AutomobileRepairShop.objects.filter(pk=shop_id)
    data = serializers.serialize('xml', shop_record)
    return HttpResponse(data)
