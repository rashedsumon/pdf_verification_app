"""
data_loader.py
Automatically download the PDF dataset from KaggleHub into ./data/
Usage:
    python data_loader.py
"""

import os
import kagglehub

# Download latest version of PDF dataset
dataset_path = kagglehub.dataset_download("manisha717/dataset-of-pdf-files")

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

print("Path to dataset files:", dataset_path)
