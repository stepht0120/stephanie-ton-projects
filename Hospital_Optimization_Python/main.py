#import packages
import logging as lg
from part1_etl.extract import extract
from part1_etl.load import load_data
from part1_etl.transform import transform
from part2_analysis.evaluate import stats
from part2_analysis.model import severity_regression_model, cpt_service_regression_model
from part3_vis.visualizations import severity_histogram, service_histogram, service_stacked_bar, severity_stacked_bar
logger = lg.getLogger(__name__)

def main():
    # logging messages
    lg.basicConfig(filename='myapp.log', level=lg.INFO)
    logger.info('Started.')
    logger.debug('Debugging message.')
    logger.info('Code is running.')
    logger.warning('Warning message.')
    logger.error('Error message.')
    logger.critical('Critical message.')
    logger.info('Finished.')

    # part 1: etl
    extract()
    load_data()
    hd_df_clean, or_df_clean = transform()

    # part 2: analysis
    # print statistics
    avg_stay, most_common_ccs, min_mod_avg_stay, maj_ext_avg_stay, emer_urg_avg_stay, ele_avg_stay, newb_avg_stay, most_common_ccs_procedure, avg_or_time, most_common_service, most_common_cpt_service = stats(hd_df_clean, or_df_clean)
    print("\n")
    print(f"Average hospital stay: {avg_stay} days.")
    print(f"Most common CCS Diagnosis: {most_common_ccs}.")
    print(f"Average hospital stay (illness severity level of minor or moderate): {min_mod_avg_stay} days.")
    print(f"Average hospital stay (illness severity level of major or extreme): {maj_ext_avg_stay} days.")
    print(f"Average hospital stay (emergency and urgent admission):  {emer_urg_avg_stay} days.")
    print(f"Average hospital stay (elective admission): {ele_avg_stay} days.")
    print(f"Average hospital stay (newborn admission): {newb_avg_stay} days.")
    print(f"Most common CCS Procedure: {most_common_ccs_procedure}.")
    print(f"Average booked OR time: {avg_or_time} minutes.")
    print(f"Most common OR service: {most_common_service}.")
    print(f"Most coming OR CPT service: {most_common_cpt_service}.")
    print("\n")

    # regression model
    severity_regression_model()
    cpt_service_regression_model()

    # part 3: visualizations
    # creation of visualizations
    # histograms
    severity_histogram()
    service_histogram()

    # stacked bar graphs
    severity_stacked_bar()
    service_stacked_bar()

if __name__ == '__main__':
    main()