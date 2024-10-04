# Hospital Optimization (Python)

1. Project Overview
1a. Business Problem
My business problem focuses on optimizing hospital operations. Currently, there is a problem with hospital wait times and also general efficiency of hospital operations. The clinical workflow of the hospital is very important because it also affects the effective usage of the available resources, which include bed utilization, quality of care, and patient flow. Optimizing the hospital operations will benefit many people to ensure effectiveness of care and lessen wait times, which in turn lessens the risk of critical health issues due to wait times. It will also help with administrative operations and also non-emergency situations and better the traffic flow for any situation. Using data analytics, I am able to predict the length of stay and operating room time of a patient based on services, severity levels, and admission types to allocate resources effectively, such as staffing schedules, bed usage, and operating room schedules. The combination of all of these solutions will result in reduced wait times, better resource utilization and allocation, and improved patient satisfaction. 


1b. Datasets Used
The datasets that I am using are ones that relate to hospital operation data, patient admission and discharge data, staffing schedules. I am focusing on the patient admission and discharge data and hospital operation data to look into reducing patient wait time and resource allocation. For sourcing the data, I ended up relying on public records. There are limited datasets available to the public because it would be violating the privacy of patients to some extent. 
The datsets I am using are from data.world. The first one is called “Hospital Inpatient Discharges”, highlighting the discharge level detail on patient characteristics, diagnoses, treatments, services, and charges. The data is tidy and I found it via Google Search. I should be able to use this data to examine trends of medical conditions to effectively reallocate resources. The other dataset I found is called “Operating Room Utilization”. This dataset was recorded with the intent on providing useful information to potential areas of inefficiency and utilization. I believe that this dataset will provide me with a lot of findings for my business problem. The data is tidy and I found it via Google Search. I believe that I will be able to use this data to examine and analyze the time spent in the operating room based on medical condition and effective reallocate services and doctors to reduce patient wait times.

2. Setup Instructions
2a. How to Access
This project will be updated on Github. The repository that this project is in is called "inst414-final-project-stephanie-ton" and will be public for others to see. To become a collaborator, please email ston1@umd.edu.

2b. How to Clone
Before you can clone this project, you will need to have Github Desktop and Visual Studio Code (VS Code) downloaded. This way, you will be able to access the code and successfully clone it to your local drive. 
Using Github, you can clone the project or fork the project to make your own edits. Using VS Code, you can view, run, and edit the code I have created. 
There are no other applications you need to download to successfully run my code, and no other dependenies, unless you would like to view the data included in this project, which then you will need an application that can read CSV files and PNG files.

3. Running the Project
In order to run this project, all you will need to do is run the main.py file. It should have every aspect loaded in to sucessfully see how my project works and the outcome. In order to see each stage, you can view each stage's py file (ETL, analysis, visualization).

4. Code Package sStructure 
data/: raw and processed data files, pictures, and data dictionaries and reference tables (extracted, processed, outputs, reference-tables)
part1_etl/: py files for the ETL process (extract, transform, load)
part2_analysis/: py files for analyzing data through statistical models and regression analysis
part3_vis/: py file for creating histograms based on different categories