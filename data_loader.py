"""
data_loader.py
Automatically download the PDF dataset from KaggleHub into ./data/
"""

import os
import kagglehub

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Download latest version of PDF dataset
dataset_path = kagglehub.dataset_download("manisha717/dataset-of-pdf-files", extract=True)

print("Path to dataset files:", dataset_path)
