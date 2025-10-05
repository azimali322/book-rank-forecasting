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
    
    # Kaggle dataset identifier (using publicly accessible dataset)
    dataset_name = "sid321axn/beijing-multisite-airquality-data-set"
    
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

# Appliances Energy and ETT datasets removed - focusing on Beijing Air Quality only

def main():
    """
    Main function to download Beijing Air Quality dataset for multivariate time series analysis
    """
    print("=== BEIJING AIR QUALITY DATASET DOWNLOADER ===")
    print("This script downloads the Beijing Multi-Site Air-Quality dataset for feature engineering and transition-based forecasting")
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
    
    print("\nAvailable dataset:")
    print("1. Beijing Multi-Site Air-Quality Data")
    print("   - Features: PM2.5, PM10, SO2, NO2, CO, O3, temperature, pressure, dew point, wind speed")
    print("   - Time resolution: Hourly")
    print("   - Sites: 12 monitoring stations")
    print("   - Period: 2013-2017")
    print("   - Target: PM2.5 concentration")
    print()
    
    # Download Beijing Air Quality dataset
    print("Downloading Beijing Multi-Site Air-Quality Data...")
    download_beijing_air_quality()
    
    print("\n✅ Download process completed!")
    print("Beijing Air Quality dataset is available in the 'data_multivariate/' directory")
    print("You can now use this dataset for multivariate time series analysis")

if __name__ == "__main__":
    main()
