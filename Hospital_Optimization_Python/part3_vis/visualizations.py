import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from part1_etl.transform import transform

def severity_histogram():
    '''
    creates histogram based on the length of patient stay and the severvity level of the patient. 
    '''
    # loading in data
    hd_df_clean, or_df_clean = transform()

    # creating severity vs length of stay histogram
    # creating dataframes
    length_of_stay = hd_df_clean['Length of Stay']
    severity_level = hd_df_clean['APR Severity of Illness Description']

    # creating histogram
    plt.figure(figsize=(12, 8))

    # list of severity of categories
    severity_categories = ['Minor', 'Moderate', 'Major', 'Extreme']
    for sev in severity_categories:
        plt.hist(length_of_stay[severity_level == sev], bins = 30, alpha = 0.5, label = f'Severity: {sev}')

    # histogram labels
    plt.xlabel('Length of Stay (days)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Length of Hospital Stay by Severity')
    plt.legend()
    plt.grid(True)

    # save histogram to data/outputs
    plt.savefig('data/outputs/histogram_by_severity.png')
    plt.show()


def service_histogram():
    '''
    creates histogram based on service categories and booked OR time.
    '''
    # loading in data
    hd_df_clean, or_df_clean = transform()

    # creating dataframes
    booked_time = or_df_clean['Booked Time (min)']
    service = or_df_clean['Service']

    # creating histogram
    plt.figure(figsize=(12, 8))

    # list of admission of categories
    service_categories = ['Podiatry', 'Orthopedics', 'Ophthalmology', 'OBGYN', 'Urology', 'Plastic', 
                          'Vascular', 'General', 'ENT', 'Pediatrics']
    for s in service_categories:
        plt.hist(booked_time[service == s], bins = 30, alpha = 0.5, label = f'Service: {s}')

    # histogram labels
    plt.xlabel('Booked OR Time (min)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Booked OR Time by OR Service')
    plt.legend()
    plt.grid(True)

    # save histogram to data/outputs
    plt.savefig('data/outputs/histogram_by_or_service.png')
    plt.show()


def severity_stacked_bar():
    '''
    creates stacked bar graph based on severity illness levels and type of admission.
    '''

    # Load the CSV file
    hd_df_clean, or_df_clean = transform()

    grouped_df = hd_df_clean.groupby('Length of Stay')['APR Severity of Illness Description'].sum().reset_index()

    # Pivot the data for stacking
    pivot_df = hd_df_clean.pivot_table(index='APR Severity of Illness Description', columns='Type of Admission', aggfunc='size', fill_value=0)

    # Plot the stacked bar graph
    pivot_df.plot(kind='bar', stacked=True)
    plt.xlabel('Severity Level')
    plt.ylabel('Hospital Admissions')
    plt.title('Stacked Bar Graph of Length of Stay by Severity Level')
    plt.savefig('data/outputs/stackedbar_by_severity.png')
    plt.show()

def service_stacked_bar():
    '''
    creates stacked bar graph based on service and booked OR time.
    '''
    # Load the CSV file
    hd_df_clean, or_df_clean = transform()

    grouped_df = or_df_clean.groupby('CPT Description')['Service'].sum().reset_index()

    # Pivot the data for stacking
    pivot_df = or_df_clean.pivot_table(index='Service', columns='Booked Time (min)', aggfunc='size', fill_value=0)

    # Plot the stacked bar graph
    pivot_df.plot(kind='bar', stacked=True)
    plt.xlabel('Service')
    plt.ylabel('OR Admissions')
    plt.title('Stacked Bar Graph of Booked OR Time by Service')
    plt.savefig('data/outputs/stackedbar_by_or_service.png')
    plt.show()