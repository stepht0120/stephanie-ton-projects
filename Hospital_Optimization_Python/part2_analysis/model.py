import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from part1_etl.transform import transform
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor

def severity_regression_model():
    '''
    creates regression performance models on severity levels and length of stay and prints out results. 
    creates regression plot on severity levels and length of stay and saves it to data/outputs.
    '''
    # regression performance on severity levels and length of stay
    # load in data
    hd_df_clean, or_df_clean = transform()

    X = hd_df_clean[['APR Severity of Illness Code']] 
    y = hd_df_clean['Length of Stay']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Standardize features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train models
    models = {
        "Linear Regression for Length of Stay VS Severity": LinearRegression(),
        "Decision Tree Regression Length of Stay VS Severity": DecisionTreeRegressor()
    }

    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        results[name] = {
            "MAE": mean_absolute_error(y_test, y_pred),
            "MSE": mean_squared_error(y_test, y_pred),
            "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
            "R^2": r2_score(y_test, y_pred)
        }

    # Print results
    for model_name, metrics in results.items():
        print(f"{model_name}:")
        for metric_name, value in metrics.items():
            print(f"  {metric_name}: {value:.2f}")
        print()

    print("\n")

    # regression model for length of stay vs severity level
    sns.regplot(x='Length of Stay', y='APR Severity of Illness Code', data=hd_df_clean, ci=95)
    plt.xlabel('Length of Stay (days)')
    plt.ylabel('Severity of Illness')
    plt.title('Regression Plot of Length of Hospital Stay vs Severity of Illness')
    plt.savefig('data/outputs/regression_or_len_stay_vs_severity.png')
    plt.show()


def cpt_service_regression_model():
    '''
    creates regression performance models on CPT services and booked OR time and prints out results. 
    creates regression plot on CPT services and booked OR time and saves it to data/outputs.
    '''
    # regression performance model of booked OR time and CPT service
    # load data
    hd_df_clean, or_df_clean = transform()
    a = or_df_clean[['CPT Code']] 
    b = or_df_clean['Booked Time (min)']

    # Split the data
    a_train, a_test, b_train, b_test = train_test_split(a, b, test_size=0.3, random_state=42)

    # Standardize features
    scaler = StandardScaler()
    a_train = scaler.fit_transform(a_train)
    a_test = scaler.transform(a_test)

    # Train models
    models = {
        "Linear Regression for Booked OR Time VS CPT Service": LinearRegression(),
        "Decision Tree Regression for Booked OR Time VS CPT Service": DecisionTreeRegressor()
    }

    results = {}
    for name, model in models.items():
        model.fit(a_train, b_train)
        b_pred = model.predict(a_test)
        results[name] = {
            "MAE": mean_absolute_error(b_test, b_pred),
            "MSE": mean_squared_error(b_test, b_pred),
            "RMSE": np.sqrt(mean_squared_error(b_test, b_pred)),
            "R^2": r2_score(b_test, b_pred)
        }

    # Print results
    for model_name, metrics in results.items():
        print(f"{model_name}:")
        for metric_name, value in metrics.items():
            print(f"  {metric_name}: {value:.2f}")
        print()

    print("\n")
    
    # regression model for booked time in OR vs CPT service
    sns.regplot(x='Booked Time (min)', y='CPT Code', data=or_df_clean, ci=95)
    plt.xlabel('Booked Time (min)')
    plt.ylabel('CPT Code')
    plt.title('Regression Plot of Booked OR Time vs OR CPT Service')
    plt.savefig('data/outputs/regression_or_booked_time_vs_cpt.png')
    plt.show()
    