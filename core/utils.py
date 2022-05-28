import pandas as pd
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
