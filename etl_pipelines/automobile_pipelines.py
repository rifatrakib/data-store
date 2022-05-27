import pandas as pd
import os


def process_automobile_data():
    data_files = os.listdir('raw-data/csv/automobile/')
    df = pd.DataFrame()
    for data_file in data_files:
        segment_df = pd.read_csv(f'raw-data/csv/automobile/{data_file}', sep='|')
        df = pd.concat([df, segment_df])
    
    df['license_expiration'] = df['license_expiration'].astype('datetime64')
    df = df.rename(columns={'id': 'shop_id'}).drop(columns=['Unnamed: 0'])
    return df
