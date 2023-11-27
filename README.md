# Project: Predict Danish properties prices using Clustering  Methods

## Description

This project was completed in place of the 02807 Computational Tools final assignment.

## Contributors

Shakir Maytham Shaker - s230553
Iakovos Kyvelos - s232480
Evangelos Kalimantzalis Lianas - s210260
Myrsini Gkolemi - s233091

## Data Collection:
- Scrape a dataset of property sales with relevant features 
To do that, we first used DAWA endpoint and then we scrapped property information from [boligsiden.dk](https://www.boligsiden.dk/) using the addressses gathered from the [API](https://dawadocs.dataforsyningen.dk/dok/api#adresser-1).
The [scripts](/scripts/) directory includes all the scripts used for the automation of the process and [scraping](/src/scraping/) directory has all the necessary classes used for crawling data as well as [main](/src/scraping/main.py) which is the entry point for our scrapping.

## Feature Engineering:
- TODO

## Clustering with k-means:
- TODO

## Price Prediction within Clusters:
- TODO

## Visualization:
- TODO

## Setup

There were some issues installing ```aiohttp```. With Python 3.11, there weren't any issues with the default version installed via pip. 

Create an environment with the environment manager (e.g. venv, miniconda) of your choice and then install the packages using the following command:

```bash
pip install -r requirements.txt
```

## Overall structure of the Project

```sh
.
├── data
│   ├── converted_data
│   │   ├── 101_properties_clean.csv
│   │   ├── 147_properties_clean.csv
│   │   ├── 153_properties_clean.csv
│   │   ├── 155_properties_clean.csv
│   │   ├── 157_properties_clean.csv
│   │   ├── 159_properties_clean.csv
│   │   ├── 161_properties_clean.csv
│   │   ├── 163_properties_clean.csv
│   │   ├── 165_properties_clean.csv
│   │   ├── 167_properties_clean.csv
│   │   ├── 169_properties_clean.csv
│   │   ├── 173_properties_clean.csv
│   │   ├── 175_properties_clean.csv
│   │   ├── 183_properties_clean.csv
│   │   ├── 187_properties_clean.csv
│   │   ├── 190_properties_clean.csv
│   │   ├── 201_properties_clean.csv
│   │   ├── 210_properties_clean.csv
│   │   ├── 217_properties_clean.csv
│   │   ├── 219_properties_clean.csv
│   │   ├── 223_properties_clean.csv
│   │   ├── 230_properties_clean.csv
│   │   ├── 260_properties_clean.csv
│   │   └── 270_properties_clean.csv
│   ├── processed_data
│   │   ├── cleaned_data.csv
│   │   ├── clustered_data.csv
│   │   ├── concatenated_df.csv
│   │   └── preprocessed_data.csv
│   └── raw_data
│       ├── 101_properties_clean.csv
│       ├── 147_properties_clean.csv
│       ├── 153_properties_clean.csv
│       ├── 155_properties_clean.csv
│       ├── 157_properties_clean.csv
│       ├── 159_properties_clean.csv
│       ├── 161_properties_clean.csv
│       ├── 163_properties_clean.csv
│       ├── 165_properties_clean.csv
│       ├── 167_properties_clean.csv
│       ├── 169_properties_clean.csv
│       ├── 173_properties_clean.csv
│       ├── 175_properties_clean.csv
│       ├── 183_properties_clean.csv
│       ├── 187_properties_clean.csv
│       ├── 190_properties_clean.csv
│       ├── 201_properties_clean.csv
│       ├── 210_properties_clean.csv
│       ├── 217_properties_clean.csv
│       ├── 219_properties_clean.csv
│       ├── 223_properties_clean.csv
│       ├── 230_properties_clean.csv
│       ├── 260_properties_clean.csv
│       └── 270_properties_clean.csv
├── notebooks
│   ├── dataExploration.ipynb
│   ├── kMeans.ipynb
│   └── machineLearning.ipynb
├── plots
│   ├── denmark_property_combined_map.html
│   ├── Denmark_property_map.html
│   ├── rmsescores.png
│   └── sqm_std.png
├── README.md
├── requirements.txt
├── scripts
│   ├── count.sh
│   ├── postprocess.sh
│   ├── README.md
│   └── script.sh
├── src
    ├── preprocessing
    │   ├── dataCleaning.py
    │   └── featureEngineering.py
    └── scraping
        ├── danishaddresscrawler.py
        ├── jsonmerger.py
        ├── jsonprocessor.py
        ├── main.py
        ├── propertycrawler.py
        ├── README.md
        └── torhandler.py
```