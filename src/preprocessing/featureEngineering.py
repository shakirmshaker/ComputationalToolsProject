import pandas as pd
import os 
import re

os.chdir('src/preprocessing')

cleaned_data = pd.read_csv('../../data/processed_data/cleaned_data.csv')

def feature_eniginering(df):

    def extract_last_price(s):
        last_price_match = re.search(r'lastPrice:(\d+)', s)
        return int(last_price_match.group(1)) if last_price_match else None

    df['lastPrice'] = df['props_pageProps_dataLayer_detailMetaData'].apply(extract_last_price)
    df['sqm_price'] = df['lastPrice'] / df['props_pageProps_address_buildings_0_housingArea']

    df['props_pageProps_address_events_0_at'] = pd.to_datetime(df['props_pageProps_address_events_0_at'])

    df['years_from_today'] = pd.Timestamp.now().year - df['props_pageProps_address_events_0_at'].dt.year

    df.drop('props_pageProps_dataLayer_detailMetaData', axis=1, inplace=True)

    # Drop rows where it was not possible to extract price (only 1)
    df.dropna(inplace = True)

    # Manuel outlier
    df.drop(18373, inplace=True)

    # Penalitize old transactions as a correction for inflation and other economic factors. 
    df['years_from_today_weighted'] = df['years_from_today'] ** 2

    # Focus on "parcelhuse"    
    property_types = ['Fritliggende enfamilieshus (parcelhus)']
    df = df[df['props_pageProps_address_buildings_0_buildingName'].isin(property_types)]

    return df

preprocessed_data = feature_eniginering(cleaned_data)

preprocessed_data.to_csv('../../data/processed_data/preprocessed_data.csv', index = False)