import json
from datetime import datetime
from django.shortcuts import render
from django.core import serializers
from realestate.models import Property, Building
from django.http import HttpResponse, JsonResponse


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
