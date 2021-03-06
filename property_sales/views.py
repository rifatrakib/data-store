import os
import json
import pandas as pd
from datetime import datetime
from django.core import serializers
from core.decorators import admin_only
from property_sales.models import SalesRecord
from django.contrib.gis.geos import GEOSGeometry
from core.utils import process_property_sales_data
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


@admin_only
def generate_page_numbers(request):
    file_names = os.listdir('raw-data/csv/property/')
    page_count = list(range(1, len(file_names) + 1))
    return render(request, 'property_sales/index.html', {'page_count': page_count})


@admin_only
def build_property_sales_data(request, segment):
    records = process_property_sales_data(segment)
    for record in records:
        geo_coordinates = record.get('geo_coordinates', None)
        point_data = GEOSGeometry(json.dumps(geo_coordinates)) if type(geo_coordinates) == dict else None
        item = SalesRecord(
            sales_number=record.get('sales_number', None),
            serial_number=record.get('serial_number', None),
            list_year=record.get('list_year', None),
            town=record.get('town', None),
            address=record.get('address', None),
            assessed_value=record.get('assessed_value', None),
            sales_amount=record.get('sales_amount', None),
            sales_ratio=record.get('sales_ratio', None),
            property_type=record.get('property_type', None),
            residential_type=record.get('residential_type', None),
            non_use_code=record.get('non_use_code', None),
            assessor_remarks=record.get('assessor_remarks', None),
            opm_remarks=record.get('opm_remarks', None),
            location=point_data,
        )
        if pd.notna(record.get('date_recorded')):
            item.date_recorded = str(record.get('date_recorded', None))
        item.save()
    return render(request, 'property_sales/sales-adminer.html')


def get_property_sales_page(request, page=1):
    start, end = (page-1) * 100, page * 100
    records = SalesRecord.objects.all().order_by('id')[start:end]
    total_pages = SalesRecord.objects.all().count() // 100
    return render(request, 'property_sales/sales.html', {'records': records, 'total_pages': range(1, total_pages+1)})


def get_property_sales_as_json(request, sales_id):
    sales_record = SalesRecord.objects.filter(pk=sales_id)
    data = json.loads(serializers.serialize('geojson', sales_record))
    response = {
        'source': request.build_absolute_uri(),
        'headers': dict(request.headers),
        'api': 'public',
        'identifier': sales_id,
        'success': True,
        'data': data,
        'format': 'text/json',
        'timestamp': str(datetime.utcnow()) + ' UTC',
    }
    return JsonResponse(response)


def get_property_sales_as_xml(request, sales_id):
    sales_record = SalesRecord.objects.filter(pk=sales_id)
    data = serializers.serialize('xml', sales_record)
    return HttpResponse(data)
