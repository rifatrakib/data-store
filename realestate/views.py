import os
import json
from datetime import datetime
from django.shortcuts import render
from django.core import serializers
from core.decorators import admin_only
from core.utils import process_eiendom_data, process_eiendom_adr_data, process_bygg_data
from realestate.models import Property, PropertyAddress, Building
from django.http import HttpResponse, JsonResponse


@admin_only
def generate_property_page_numbers(request):
    file_names = os.listdir('raw-data/csv/eiendom/')
    page_count = list(range(1, len(file_names) + 1))
    return render(request, 'realestate/admin-property.html', {'page_count': page_count})


@admin_only
def build_property_data(request, segment):
    properties = process_eiendom_data(segment)
    for property in properties:
        Property.objects.create(**property)
    return render(request, 'realestate/property-adminer.html')


@admin_only
def generate_property_address_page_numbers(request):
    file_names = os.listdir('raw-data/csv/eiendom_adr/')
    page_count = list(range(1, len(file_names) + 1))
    return render(request, 'realestate/admin-property-address.html', {'page_count': page_count})


@admin_only
def build_property_address_data(request, segment):
    property_addresses = process_eiendom_adr_data(segment)
    for address in property_addresses:
        PropertyAddress.objects.create(**address)
    return render(request, 'realestate/property-address-adminer.html')


@admin_only
def generate_building_page_numbers(request):
    file_names = os.listdir('raw-data/csv/bygg/')
    page_count = list(range(1, len(file_names) + 1))
    return render(request, 'realestate/admin-building.html', {'page_count': page_count})


@admin_only
def build_building_data(request, segment):
    buildings = process_bygg_data(segment)
    for building in buildings:
        Building.objects.create(**building)
    return render(request, 'realestate/building-adminer.html')


def get_property_page(request, page=1):
    start, end = (page-1) * 100, page * 100
    properties = Property.objects.all().order_by('id')[start:end]
    total_pages = Property.objects.all().count() // 100
    return render(request, 'realestate/properties.html', {'properties': properties, 'total_pages': range(1, total_pages+1)})


# not tested yet
def get_building_page(request, page=1):
    start, end = (page-1) * 100, page * 100
    buildings = Building.objects.all().order_by('id')[start:end]
    total_pages = Building.objects.all().count() // 100
    return render(request, 'realestate/buildings.html', {'buildings': buildings, 'total_pages': range(1, total_pages+1)})


def get_property_as_json(request, property_id):
    property_record = Property.objects.filter(pk=property_id)
    data = json.loads(serializers.serialize('geojson', property_record))
    response = {
        'source': request.build_absolute_uri(),
        'headers': dict(request.headers),
        'api': 'public',
        'identifier': property_id,
        'success': True,
        'data': data,
        'format': 'text/json',
        'timestamp': str(datetime.utcnow()) + ' UTC',
    }
    return JsonResponse(response)


def get_building_as_json(request, building_id):
    building_record = Building.objects.filter(pk=building_id)
    data = json.loads(serializers.serialize('geojson', building_record))
    response = {
        'source': request.build_absolute_uri(),
        'headers': dict(request.headers),
        'api': 'public',
        'identifier': building_id,
        'success': True,
        'data': data,
        'format': 'text/json',
        'timestamp': str(datetime.utcnow()) + ' UTC',
    }
    return JsonResponse(response)


def get_property_as_xml(request, property_id):
    property_record = Property.objects.filter(pk=property_id)
    data = serializers.serialize('xml', property_record)
    return HttpResponse(data)


def get_building_as_xml(request, building_id):
    building_record = Building.objects.filter(pk=building_id)
    data = serializers.serialize('xml', building_record)
    return HttpResponse(data)
