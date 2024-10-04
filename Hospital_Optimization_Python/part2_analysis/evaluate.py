import pandas as pd
import matplotlib.pyplot as plt
from part1_etl.transform import transform 


def stats(hd_df_clean, or_df_clean):
    '''
    calculate statistics from dataset.

    returns:
        formatted_avg_stay: average hospital stay for patient in days
        most_common_ccs: most common Clinical Classifications Software (CCS) diagnosis 
        formatted_min_mod_avg_stay: average hospital stay for patient with minor and moderate illness severity levels in days
        formatted_maj_ext_avg_stay: average hospital stay for patient with major and extreme illness severity levels in days
        formatted_emer_urg_avg_stay: average hospital stay for patient with emergency and urgent admission in days
        formatted_ele_avg_stay: average hospital stay for patient with elective admission in days
        formatted_newb_avg_stay: average hospital stay for patient with newborn admission in days
        formatted_avg_or_time: average operating room time in minutes
        most_common_service: most common operating room service

    '''
    # loading in data
    hd_df_clean, or_df_clean = transform()

    # average length of patient stay
    avg_length_of_stay = hd_df_clean['Length of Stay'].mean()
    formatted_avg_stay = f"{avg_length_of_stay:.2f}"
    
    # most common CCS diagnosis
    most_common_ccs = hd_df_clean["CCS Diagnosis Description"].mode()[0]
    
    # average length of hospital stay based on severity level (minor and moderate)
    minor_or_moderate_df = hd_df_clean[hd_df_clean['APR Severity of Illness Description'].isin(['Minor', 'Moderate'])]
    minor_moderate_avg_stay = minor_or_moderate_df['Length of Stay'].mean()
    formatted_min_mod_avg_stay = f"{minor_moderate_avg_stay:.2f}"
    
    # average length of hospital stay based on severity level (major and extreme)
    major_extreme_df = hd_df_clean[hd_df_clean['APR Severity of Illness Description'].isin(['Major', 'Extreme'])]
    major_extreme_avg_stay = major_extreme_df['Length of Stay'].mean()
    formatted_maj_ext_avg_stay = f"{major_extreme_avg_stay:.2f}"
    
    # average length of hospital stay based on type of admission (emergency and urgent)
    emer_urg_df = hd_df_clean[hd_df_clean['Type of Admission'].isin(['Emergency', 'Urgent'])]
    emer_urg_avg_stay = emer_urg_df['Length of Stay'].mean()
    formatted_emer_urg_avg_stay = f"{emer_urg_avg_stay:.2f}"

    # average length of hospital stay based on type of admission (elective)
    ele_df = hd_df_clean[hd_df_clean['Type of Admission'].isin(['Elective'])]
    ele_avg_stay = ele_df['Length of Stay'].mean()
    formatted_ele_avg_stay = f"{ele_avg_stay:.2f}"

    # average length of hospital stay based on type of admission (newborn)
    newb_df = hd_df_clean[hd_df_clean['Type of Admission'].isin(['Newborn'])]
    newb_avg_stay = newb_df['Length of Stay'].mean()
    formatted_newb_avg_stay = f"{newb_avg_stay:.2f}"

    # most common CCS procedure
    most_common_ccs_procedure = hd_df_clean["CCS Procedure Description"].mode()[0]

    # average length in booked operating room in minutes
    avg_or_time = or_df_clean['Booked Time (min)'].mean()
    formatted_avg_or_time = f"{avg_or_time:.2f}"

    # most common operating room service
    most_common_service = or_df_clean["Service"].mode()[0]

    # most common CPT service
    most_common_cpt_service = or_df_clean["CPT Description"].mode()[0]

    return formatted_avg_stay, most_common_ccs, formatted_min_mod_avg_stay, formatted_maj_ext_avg_stay, formatted_emer_urg_avg_stay, formatted_ele_avg_stay, formatted_newb_avg_stay, most_common_ccs_procedure, formatted_avg_or_time, most_common_service, most_common_cpt_service
