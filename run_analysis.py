#!/usr/bin/env python3
"""
Main script to run the complete time series forecasting analysis
"""

import os
import sys
import subprocess
from pathlib import Path

def run_notebook(notebook_path):
    """Run a Jupyter notebook"""
    print(f"Running {notebook_path}...")
    try:
        subprocess.run([
            "jupyter", "nbconvert", "--execute", "--to", "notebook",
            "--inplace", str(notebook_path)
        ], check=True)
        print(f"✓ {notebook_path} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error running {notebook_path}: {e}")
        return False

def check_requirements():
    """Check if required packages are installed"""
    required_packages = [
        "pandas", "numpy", "matplotlib", "seaborn", "scikit-learn",
        "statsmodels", "prophet", "tensorflow", "xgboost", "lightgbm"
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("Missing required packages:")
        for package in missing_packages:
            print(f"- {package}")
        print("\nInstall missing packages with:")
        print("pip install -r requirements.txt")
        return False
    
    return True

def main():
    """Main function"""
    print("Book Rank Forecasting Analysis")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not Path("requirements.txt").exists():
        print("Error: requirements.txt not found. Please run from project root.")
        return
    
    # Check requirements
    if not check_requirements():
        return
    
    # Check if data exists
    data_dir = Path("data")
    if not (data_dir / "amazon_com_extras.csv").exists():
        print("Dataset not found. Please run:")
        print("python data/download_kaggle_data.py")
        return
    
    # Define notebook sequence
    notebooks = [
        "notebooks/01_data_exploration.ipynb",
        "notebooks/02_time_series_analysis.ipynb",
        "notebooks/03_model_training.ipynb",
        "notebooks/04_model_evaluation.ipynb"
    ]
    
    # Run notebooks in sequence
    print("\nRunning analysis notebooks...")
    for notebook in notebooks:
        if not Path(notebook).exists():
            print(f"Warning: {notebook} not found, skipping...")
            continue
        
        if not run_notebook(notebook):
            print(f"Analysis stopped due to error in {notebook}")
            return
    
    print("\n" + "=" * 40)
    print("Analysis completed successfully!")
    print("\nResults available in:")
    print("- results/ directory")
    print("- plots/ directory")
    print("\nReview the final model comparison and select the best model for deployment.")

if __name__ == "__main__":
    main()
