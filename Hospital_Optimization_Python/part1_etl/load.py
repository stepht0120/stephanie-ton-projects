import pandas as pd
from part1_etl.extract import extract

def load_data():
    '''
    loads in data from data/extract and loads in certain columns to use and saves data to data/processed.
    '''
    # assigning file paths
    hd_file_path, or_file_path = extract()

    # loading in certain columns
    hd_columns_to_load = ['Length of Stay', 'Type of Admission', 'Patient Disposition', 
                        'Discharge Year', 'CCS Diagnosis Code', 'CCS Diagnosis Description', 'CCS Procedure Description', 
                        'APR Severity of Illness Code', 'APR Severity of Illness Description', 'APR Risk of Mortality']
    or_columns_to_load = ['Date', 'OR Suite', 'Service', 'CPT Code', 'CPT Description', 'Booked Time (min)', 'OR Schedule', 
                        'Wheels In', 'Start Time', 'End Time', 'Wheels Out']

    hd_df = pd.read_csv(hd_file_path, usecols = hd_columns_to_load)
    or_df = pd.read_csv(or_file_path, usecols = or_columns_to_load)

    # save dataframes to data/processed
    hd_df.to_csv('data/processed/hospitaldischarge_processed.csv')
    or_df.to_csv('data/processed/operatingroom_processed.csv')

    return hd_df, or_df