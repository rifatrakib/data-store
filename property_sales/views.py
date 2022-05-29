import os
import json
import pandas as pd
from django.shortcuts import render
from core.decorators import admin_only
from property_sales.models import SalesRecord
from django.contrib.gis.geos import GEOSGeometry
from core.utils import process_property_sales_data


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
