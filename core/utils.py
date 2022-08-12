import pandas as pd
import numpy as np
import json


def process_automobile_data(segment_number):
    start = (segment_number - 1) * 10000
    end = segment_number * 10000
    directory = f'raw-data/csv/automobile/automobile-data-{start}-{end}.csv'
    df = pd.read_csv(directory, sep='|')
    
    df['license_expiration'] = df['license_expiration'].astype('datetime64')
    df = df.rename(columns={'id': 'shop_number'}).drop(columns=['Unnamed: 0'])
    
    point_condition = df['geo_coordinates'].notna()
    df['geo_coordinates'] = df['geo_coordinates'].str.replace('\'', '\"')
    df['geo_coordinates'] = df[point_condition]['geo_coordinates'].apply(json.loads).map(lambda x: x[0])
    df['geo_type'] = df[point_condition]['geo_coordinates'].map(lambda x: x['type']).str.upper()
    df['lon'] = df[point_condition]['geo_coordinates'].map(lambda x: x['coordinates'][0])
    df['lat'] = df[point_condition]['geo_coordinates'].map(lambda x: x['coordinates'][1])
    
    return df.to_dict(orient='records')


def process_property_sales_data(segment_number):
    start = (segment_number - 1) * 10000
    end = segment_number * 10000
    directory = f'raw-data/csv/property/property-data-{start}-{end}.csv'
    df = pd.read_csv(directory, sep='|')
    
    df['date_recorded'] = df['date_recorded'].astype('datetime64')
    df = df.rename(columns={'id': 'sales_number', 'remarks': 'assessor_remarks'}).drop(columns=['Unnamed: 0'])
    
    point_condition = df['geo_coordinates'].notna()
    df['geo_coordinates'] = df['geo_coordinates'].str.replace('\'', '\"')
    df['geo_coordinates'] = df[point_condition]['geo_coordinates'].apply(json.loads).map(lambda x: x[0])
    
    return df.to_dict(orient='records')


def process_small_business_data(segment_number):
    start = (segment_number - 1) * 10000
    end = segment_number * 10000
    directory = f'raw-data/csv/business/business-data-{start}-{end}.csv'
    
    dtypes = {
        'account_number': 'str',
        'annual_report_due_date': 'str',
        'began_transacting_in_ct': 'str',
        'business_city': 'str',
        'business_country': 'str',
        'business_email_address': 'str',
        'business_name_in_state_country': 'str',
        'business_state': 'str',
        'business_street': 'str',
        'business_type': 'str',
        'business_unit': 'str',
        'business_zip_code': 'str',
        'category_survey_email_address': 'str',
        'citizenship': 'str',
        'country_formation': 'str',
        'created_on': 'str',
        'date_of_organization_meeting': 'str',
        'disable_person_owned_organization': 'boolean',
        'dissolution_date': 'str',
        'formation_place': 'str',
        'id': 'str',
        'mail_jurisdiction': 'str',
        'mailing_address': 'str',
        'mailing_international_address': 'str',
        'mailing_jurisdiction_address': 'str',
        'mailing_jurisdiction_business_city': 'str',
        'mailing_jurisdiction_business_country': 'str',
        'mailing_jurisdiction_business_state': 'str',
        'mailing_jurisdiction_business_street': 'str',
        'mailing_jurisdiction_business_unit': 'str',
        'mailing_jurisdiction_business_zip_code': 'str',
        'minority_owned_organization': 'boolean',
        'naics_code': 'str',
        'naics_sub_code': 'str',
        'name': 'str',
        'office_jurisdiction_address': 'str',
        'office_jurisdiction_business_city': 'str',
        'office_jurisdiction_business_state': 'str',
        'office_jurisdiction_business_street': 'str',
        'office_jurisdiction_business_unit': 'str',
        'office_jurisdiction_business_zip_code': 'str',
        'office_jurisdiction_country': 'str',
        'reason_for_administrative_dissolution': 'str',
        'record_address': 'str',
        'records_address_city': 'str',
        'records_address_country': 'str',
        'records_address_state': 'str',
        'records_address_street': 'str',
        'records_address_unit': 'str',
        'records_address_zip_code': 'str',
        'registration_date': 'str',
        'state_or_territory_formation': 'str',
        'status': 'str',
        'sub_status': 'str',
        'total_authorized_shares': 'Int64',
        'veteran_owned_organization': 'boolean',
        'woman_owned_organization': 'boolean',
    }
    
    date_fields = [
        'annual_report_due_date', 'began_transacting_in_ct', 'created_on',
        'date_of_organization_meeting', 'dissolution_date', 'registration_date'
    ]
    
    df = pd.read_csv(directory, sep='|', dtype=dtypes, parse_dates=date_fields)
    df = df.rename(columns={'id': 'business_identifier'}).drop(columns=['Unnamed: 0'])
    df = df.replace({np.nan: None, pd.NA: None})
    return df.to_dict(orient='records')


def process_eiendom_data(segment_number):
    start = (segment_number - 1) * 10000
    end = segment_number * 10000
    directory = f'raw-data/csv/eiendom/eiendom-{start}-{end}.csv'
    
    dtypes = {
        'EIENDOM_ID': 'Int64',
        'FYLKES_NR': 'Int64',
        'FYLKES_NAVN': 'str',
        'KOMMUNE_NR': 'Int64',
        'KOMMUNE_NAVN': 'str',
        'GNR': 'Int64',
        'BNR': 'Int64',
        'FNR': 'Int64',
        'SNR': 'Int64',
        'BRUKSNAVN': 'str',
        'ANTALL_TEIGER': 'Int64',
        'AREAL': 'float64',
        'AREALKILDE_NR': 'Int64',
        'AREALKILDE_NAVN': 'str',
        'NÆRINGS_KODE': 'str',
        'NÆRINGS_KODE_NAVN': 'str',
        'TINGLYST': 'boolean',
        'OMSETNINGSDATO': 'Int64',
        'KJOPESUM': 'float64',
        'OMSETNINGSTYPE_KODE': 'str',
        'OMSETNINGSTYPE_NAVN': 'str',
        'SAMEIE_TELLER': 'Int64',
        'SAMEIE_NEVNER': 'Int64',
        'ETABLERT_DATO': 'Int64',
        'ETABLERT_AAR': 'Int64',
        'EIENDOMSTYPE_KODE': 'Int64',
        'EIENDOMSTYPE_NAVN': 'str',
        'BYGNING_PAA_EIENDOM': 'boolean',
        'BYGNING_PAA_EIENDOM_NAVN': 'Int64',
        'ANTALL_BYGNINGER': 'Int64',
        'ANTALL_ADRESSER': 'Int64',
        'LKOORD_SYS_NR': 'Int64',
        'LKOORD_SYS_NAVN': 'str',
        'LKOOELOKX': 'float64',
        'LKOOELOKY': 'float64',
    }
    
    df = pd.read_csv(directory, dtype=dtypes).drop(columns=['Unnamed: 0'])
    df = df.replace({np.nan: None, pd.NA: None})
    df = df.rename(columns=str.lower).rename(columns={
        'eiendom_id': 'property_number',
        'fylkes_nr': 'county_number',
        'fylkes_navn': 'county_name',
        'kommune_nr': 'city_number',
        'kommune_navn': 'city_name',
    })
    return df.to_dict(orient='records')
