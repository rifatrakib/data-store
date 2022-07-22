import json
from datetime import datetime
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from realestate.models import Property


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
