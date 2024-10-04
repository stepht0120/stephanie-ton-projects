import pandas as pd

def extract():
    '''
    extracts and reads in data from data/extracted folder.
    '''
    hd_csv_file_path = 'data/extracted/hospitaldischarge.csv'
    hd_data = pd.read_csv(hd_csv_file_path)

    or_csv_file_path = 'data/extracted/operatingroom.csv'
    or_data = pd.read_csv(or_csv_file_path)

    return hd_csv_file_path, or_csv_file_path
