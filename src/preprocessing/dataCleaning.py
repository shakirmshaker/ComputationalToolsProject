import pandas as pd
import os
import re
import matplotlib.pyplot as plt
import dask.dataframe as dd 
import numpy as np
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.preprocessing import OrdinalEncoder

os.chdir('src/preprocessing')

def read_and_filter_csv_files(folder_path):

    # Columns to be read
    cols = ['props_pageProps_address_buildings_0_bathroomCondition', 
            'props_pageProps_address_buildings_0_buildingName',
            'props_pageProps_address_buildings_0_externalWallMaterial', 
            'props_pageProps_address_buildings_0_heatingInstallation',
            'props_pageProps_address_buildings_0_housingArea', 
            'props_pageProps_address_buildings_0_kitchenCondition', 
            'props_pageProps_address_buildings_0_numberOfFloors',
            'props_pageProps_address_buildings_0_numberOfToilets', 
            'props_pageProps_address_buildings_0_roofingMaterial', 
            'props_pageProps_address_buildings_0_toiletCondition',
            'props_pageProps_address_buildings_0_yearBuilt', 
            'props_pageProps_address_municipality_name', 
            'props_pageProps_address_coordinates_lat', 
            'props_pageProps_address_coordinates_lon',
            'props_pageProps_address_events_0_at',
            'props_pageProps_address_events_0_label', 
            'props_pageProps_dataLayer_virtualPagePath', 
            'props_pageProps_dataLayer_detailMetaData']

    # List to hold the filtered DataFrames
    filtered_dfs = []

    # Process each CSV file in the folder
    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            file_path = os.path.join(folder_path, file)
            df = dd.read_csv(file_path, usecols=cols, sample=10000000, assume_missing=True, dtype=str)

            # Compute to Pandas DataFrame and apply filter
            df_computed = df.compute()
            df_filtered = df_computed[df_computed['props_pageProps_address_events_0_label'] == 'Fri handel']
            
            # Find the mode and filter
            mode = df_filtered['props_pageProps_address_municipality_name'].mode()[0]
            df_filtered = df_filtered[df_filtered['props_pageProps_address_municipality_name'] == mode]            

            filtered_dfs.append(df_filtered)

    # Concatenate all DataFrames
    concatenated_df = pd.concat(filtered_dfs, ignore_index=True)
    return concatenated_df

concatenated_df = read_and_filter_csv_files('../../data/converted_data')

def convert_dtypes(concatenated_df):

    # Convert to numeric and datetime with coercion (NaN if error)
    concatenated_df['props_pageProps_address_buildings_0_housingArea'] = pd.to_numeric(concatenated_df['props_pageProps_address_buildings_0_housingArea'], errors='coerce')
    concatenated_df['props_pageProps_address_buildings_0_numberOfFloors'] = pd.to_numeric(concatenated_df['props_pageProps_address_buildings_0_numberOfFloors'], errors='coerce', downcast='integer')
    concatenated_df['props_pageProps_address_buildings_0_numberOfToilets'] = pd.to_numeric(concatenated_df['props_pageProps_address_buildings_0_numberOfToilets'], errors='coerce', downcast='integer')
    concatenated_df['props_pageProps_address_buildings_0_yearBuilt'] = pd.to_numeric(concatenated_df['props_pageProps_address_buildings_0_yearBuilt'], errors='coerce', downcast='integer')
    concatenated_df['props_pageProps_address_coordinates_lat'] = pd.to_numeric(concatenated_df['props_pageProps_address_coordinates_lat'], errors='coerce')
    concatenated_df['props_pageProps_address_coordinates_lon'] = pd.to_numeric(concatenated_df['props_pageProps_address_coordinates_lon'], errors='coerce')
    concatenated_df['props_pageProps_address_events_0_at'] = pd.to_datetime(concatenated_df['props_pageProps_address_events_0_at'], errors='coerce')

    return concatenated_df

concatenated_df = convert_dtypes(concatenated_df)
concatenated_df.to_csv('../../data/processed_data/concatenated_df.csv', index=False)

def imputation(df):

    # Ensure nan consistensy
    df = df.applymap(lambda x: np.nan if pd.isna(x) else x)

    # Separating the categorical and numerical columns
    categorical_columns = df.select_dtypes(include=['object']).columns
    numerical_columns = df.select_dtypes(exclude=['object']).columns
    numerical_columns = numerical_columns.drop('props_pageProps_address_events_0_at')

    # Impute categorical data using the most frequent value
    cat_imputer = SimpleImputer(strategy='most_frequent')
    df[categorical_columns] = cat_imputer.fit_transform(df[categorical_columns])

    # Encode categorical columns
    ordinal_encoder = OrdinalEncoder()
    df_encoded = df.copy()
    df_encoded[categorical_columns] = ordinal_encoder.fit_transform(df[categorical_columns])

    # Impute numerical data using KNN
    knn_imputer = KNNImputer(n_neighbors=5)
    df_encoded[numerical_columns] = knn_imputer.fit_transform(df_encoded[numerical_columns])

    # Decode categorical columns back to original values
    df_imputed = df_encoded.copy()
    df_imputed[categorical_columns] = ordinal_encoder.inverse_transform(df_encoded[categorical_columns])

    return df_imputed

df_imputed = imputation(concatenated_df)

df_imputed.to_csv('../../data/processed_data/cleaned_data.csv', index=False)