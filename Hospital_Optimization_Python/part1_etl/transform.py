import pandas as pd
from part1_etl.load import load_data

def transform():
    '''
    using data from data/processed folder, cleans and organizes data and saves data into data/processed.
    '''
    hd_df, or_df = load_data()

    # removing rows with missing values
    hd_df_clean = hd_df.dropna()
    or_df_clean = or_df.dropna()

    # save clean data to data/processed
    hd_df_clean.to_csv('data/processed/hospitaldischarge_clean.csv')
    or_df_clean.to_csv('data/processed/operatingroom_clean.csv')

    return hd_df_clean, or_df_clean