import os
import json
from datetime import datetime
from django.core import serializers
from django.shortcuts import render
from core.decorators import admin_only
from businesses.models import SmallBusiness
from django.http import JsonResponse, HttpResponse
from core.utils import process_small_business_data


@admin_only
def generate_page_numbers(request):
    file_names = os.listdir('raw-data/csv/business')
    page_count = list(range(1, len(file_names) + 1))
    return render(request, 'businesses/index.html', {'page_count': page_count})


@admin_only
def build_small_business_data(request, segment):
    records = process_small_business_data(segment)
    for record in records:
        SmallBusiness.objects.create(
            account_number=record.get('account_number', None),
            annual_report_due_date=record.get('annual_report_due_date', None),
            began_transacting_in_ct=record.get('began_transacting_in_ct', None),
            business_city=record.get('business_city', None),
            business_country=record.get('business_country', None),
            business_email_address=record.get('business_email_address', None),
            business_name_in_state_country=record.get('business_name_in_state_country', None),
            business_state=record.get('business_state', None),
            business_street=record.get('business_street', None),
            business_type=record.get('business_type', None),
            business_unit=record.get('business_unit', None),
            business_zip_code=record.get('business_zip_code', None),
            category_survey_email_address=record.get('category_survey_email_address', None),
            citizenship=record.get('citizenship', None),
            country_formation=record.get('country_formation', None),
            created_on=record.get('created_on', None),
            date_of_organization_meeting=record.get('date_of_organization_meeting', None),
            disable_person_owned_organization=record.get('disable_person_owned_organization', None),
            dissolution_date=record.get('dissolution_date', None),
            formation_place=record.get('formation_place', None),
            business_identifier=record.get('business_identifier', None),
            mail_jurisdiction=record.get('mail_jurisdiction', None),
            mailing_address=record.get('mailing_address', None),
            mailing_international_address=record.get('mailing_international_address', None),
            mailing_jurisdiction_address=record.get('mailing_jurisdiction_address', None),
            mailing_jurisdiction_business_city=record.get('mailing_jurisdiction_business_city', None),
            mailing_jurisdiction_business_country=record.get('mailing_jurisdiction_business_country', None),
            mailing_jurisdiction_business_state=record.get('mailing_jurisdiction_business_state', None),
            mailing_jurisdiction_business_street=record.get('mailing_jurisdiction_business_street', None),
            mailing_jurisdiction_business_unit=record.get('mailing_jurisdiction_business_unit', None),
            mailing_jurisdiction_business_zip_code=record.get('mailing_jurisdiction_business_zip_code', None),
            minority_owned_organization=record.get('minority_owned_organization', None),
            naics_code=record.get('naics_code', None),
            naics_sub_code=record.get('naics_sub_code', None),
            name=record.get('name', None),
            office_jurisdiction_address=record.get('office_jurisdiction_address', None),
            office_jurisdiction_business_city=record.get('office_jurisdiction_business_city', None),
            office_jurisdiction_business_state=record.get('office_jurisdiction_business_state', None),
            office_jurisdiction_business_street=record.get('office_jurisdiction_business_street', None),
            office_jurisdiction_business_unit=record.get('office_jurisdiction_business_unit', None),
            office_jurisdiction_business_zip_code=record.get('office_jurisdiction_business_zip_code', None),
            office_jurisdiction_country=record.get('office_jurisdiction_country', None),
            reason_for_administrative_dissolution=record.get('reason_for_administrative_dissolution', None),
            record_address=record.get('record_address', None),
            records_address_city=record.get('records_address_city', None),
            records_address_country=record.get('records_address_country', None),
            records_address_state=record.get('records_address_state', None),
            records_address_street=record.get('records_address_street', None),
            records_address_unit=record.get('records_address_unit', None),
            records_address_zip_code=record.get('records_address_zip_code', None),
            registration_date=record.get('registration_date', None),
            state_or_territory_formation=record.get('state_or_territory_formation', None),
            status=record.get('status', None),
            sub_status=record.get('sub_status', None),
            total_authorized_shares=record.get('total_authorized_shares', None),
            veteran_owned_organization=record.get('veteran_owned_organization', None),
            woman_owned_organization=record.get('woman_owned_organization', None),
        )
    return render(request, 'businesses/small-business-adminer.html')


def get_small_business_page(request, page=1):
    start, end = (page-1) * 100, page * 100
    records = SmallBusiness.objects.all().order_by('id')[start:end]
    total_pages = SmallBusiness.objects.all().count() // 100
    return render(request, 'businesses/small-business.html', {'records': records, 'total_pages': range(1, total_pages+1)})


def get_small_business_as_json(request, business_id):
    business_record = SmallBusiness.objects.filter(pk=business_id)
    data = json.loads(serializers.serialize('json', business_record))
    response = {
        'source': request.build_absolute_uri(),
        'headers': dict(request.headers),
        'api': 'public',
        'identifier': business_id,
        'success': True,
        'data': data,
        'format': 'text/json',
        'timestamp': str(datetime.utcnow()) + ' UTC',
    }
    return JsonResponse(response)


def get_repair_shops_as_xml(request, business_id):
    business_record = SmallBusiness.objects.filter(pk=business_id)
    data = serializers.serialize('xml', business_record)
    return HttpResponse(data)
