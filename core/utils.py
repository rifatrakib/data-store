import pandas as pd


def process_automobile_data(segment_number):
    start = (segment_number - 1) * 10000
    end = segment_number * 10000
    directory = f'raw-data/csv/automobile/automobile-data-{start}-{end}.csv'
    df = pd.read_csv(directory, sep='|')
    df['license_expiration'] = df['license_expiration'].astype('datetime64')
    df = df.rename(columns={'id': 'shop_id'}).drop(columns=['Unnamed: 0'])
    return df
