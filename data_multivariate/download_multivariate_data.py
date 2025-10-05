#!/usr/bin/env python3
"""
Download script for multivariate time series datasets from Kaggle
"""

import os
import kaggle
import zipfile
import shutil

def download_beijing_air_quality():
    """
    Download Beijing Multi-Site Air-Quality Data
    Features: PM2.5, PM10, SO2, NO2, CO, O3, temperature, pressure, dew point, wind speed
    """
    print("Downloading Beijing Multi-Site Air-Quality Data...")
    
    # Kaggle dataset identifier
    dataset_name = "saurabhshahane/beijing-multisite-airquality-data"
    
    try:
        # Download dataset
        kaggle.api.dataset_download_files(dataset_name, path='.', unzip=True)
        print("✅ Beijing Air Quality dataset downloaded successfully!")
        
        # Move files to data_multivariate directory
        files_to_move = [
            'PRSA_Data_20130301-20170228',
            'PRSA_Data_Aotizhongxin_20130301-20170228.csv',
            'PRSA_Data_Changping_20130301-20170228.csv',
            'PRSA_Data_Dingling_20130301-20170228.csv',
            'PRSA_Data_Dongsi_20130301-20170228.csv',
            'PRSA_Data_Guanyuan_20130301-20170228.csv',
            'PRSA_Data_Gucheng_20130301-20170228.csv',
            'PRSA_Data_Huairou_20130301-20170228.csv',
            'PRSA_Data_Nongzhanguan_20130301-20170228.csv',
            'PRSA_Data_Shunyi_20130301-20170228.csv',
            'PRSA_Data_Tiantan_20130301-20170228.csv',
            'PRSA_Data_Wanliu_20130301-20170228.csv',
            'PRSA_Data_Wanshouxigong_20130301-20170228.csv'
        ]
        
        for file in files_to_move:
            if os.path.exists(file):
                if os.path.isdir(file):
                    shutil.move(file, f'data_multivariate/{file}')
                else:
                    shutil.move(file, f'data_multivariate/{file}')
                print(f"  Moved {file} to data_multivariate/")
        
        return True
        
    except Exception as e:
        print(f"❌ Error downloading Beijing Air Quality dataset: {e}")
        return False

def download_appliances_energy():
    """
    Download Appliances Energy Prediction Data
    Features: Temperature, humidity, pressure, wind speed, visibility, etc.
    """
    print("Downloading Appliances Energy Prediction Data...")
    
    # Kaggle dataset identifier
    dataset_name = "luisblanche/appliances-energy-prediction"
    
    try:
        # Download dataset
        kaggle.api.dataset_download_files(dataset_name, path='.', unzip=True)
        print("✅ Appliances Energy dataset downloaded successfully!")
        
        # Move files to data_multivariate directory
        files_to_move = [
            'energydata_complete.csv',
            'energydata_complete.csv.zip'
        ]
        
        for file in files_to_move:
            if os.path.exists(file):
                shutil.move(file, f'data_multivariate/{file}')
                print(f"  Moved {file} to data_multivariate/")
        
        return True
        
    except Exception as e:
        print(f"❌ Error downloading Appliances Energy dataset: {e}")
        return False

def download_electricity_transformer():
    """
    Download Electricity Transformer Temperature (ETT) Data
    Features: Oil temperature, power load features
    """
    print("Downloading Electricity Transformer Temperature Data...")
    
    # Kaggle dataset identifier
    dataset_name = "laiguokun/electricity-transformer-temperature"
    
    try:
        # Download dataset
        kaggle.api.dataset_download_files(dataset_name, path='.', unzip=True)
        print("✅ ETT dataset downloaded successfully!")
        
        # Move files to data_multivariate directory
        files_to_move = [
            'ETT-small',
            'ETT-large'
        ]
        
        for file in files_to_move:
            if os.path.exists(file):
                if os.path.isdir(file):
                    shutil.move(file, f'data_multivariate/{file}')
                else:
                    shutil.move(file, f'data_multivariate/{file}')
                print(f"  Moved {file} to data_multivariate/")
        
        return True
        
    except Exception as e:
        print(f"❌ Error downloading ETT dataset: {e}")
        return False

def main():
    """
    Main function to download multivariate time series datasets
    """
    print("=== MULTIVARIATE TIME SERIES DATASET DOWNLOADER ===")
    print("This script downloads datasets suitable for feature engineering and transition-based forecasting")
    print()
    
    # Check if Kaggle API is configured
    try:
        kaggle.api.authenticate()
        print("✅ Kaggle API authenticated successfully")
    except Exception as e:
        print(f"❌ Kaggle API authentication failed: {e}")
        print("Please ensure you have:")
        print("1. Created a Kaggle account")
        print("2. Downloaded kaggle.json from your account settings")
        print("3. Placed it in ~/.kaggle/ and set permissions: chmod 600 ~/.kaggle/kaggle.json")
        return
    
    # Create data directory
    os.makedirs('data_multivariate', exist_ok=True)
    
    print("\nAvailable datasets:")
    print("1. Beijing Multi-Site Air-Quality Data (Recommended)")
    print("   - Features: PM2.5, PM10, SO2, NO2, CO, O3, temperature, pressure, dew point, wind speed")
    print("   - Time resolution: Hourly")
    print("   - Sites: 12 monitoring stations")
    print("   - Period: 2013-2017")
    print()
    print("2. Appliances Energy Prediction")
    print("   - Features: Temperature, humidity, pressure, wind speed, visibility, etc.")
    print("   - Time resolution: 10 minutes")
    print("   - Target: Energy consumption")
    print()
    print("3. Electricity Transformer Temperature (ETT)")
    print("   - Features: Oil temperature, 6 power load features")
    print("   - Time resolution: 1 hour and 15 minutes")
    print("   - Period: 2 years")
    print()
    
    # Download recommended dataset
    choice = input("Enter dataset number to download (1-3, or 'all' for all datasets): ").strip()
    
    if choice == '1' or choice.lower() == 'all':
        download_beijing_air_quality()
    
    if choice == '2' or choice.lower() == 'all':
        download_appliances_energy()
    
    if choice == '3' or choice.lower() == 'all':
        download_electricity_transformer()
    
    if choice not in ['1', '2', '3', 'all']:
        print("Invalid choice. Downloading recommended dataset (Beijing Air Quality)...")
        download_beijing_air_quality()
    
    print("\n✅ Download process completed!")
    print("Datasets are available in the 'data_multivariate/' directory")
    print("You can now use these datasets for multivariate time series analysis")

if __name__ == "__main__":
    main()
