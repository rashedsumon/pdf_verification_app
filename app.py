"""
app.py
Streamlit app to process PDFs and generate validation report.
"""

import streamlit as st
import os
from data_loader import dataset_path
from pdf_processor import process_pdf
from baseline_model import run_baseline_models
from validation_report import generate_report

st.title("PDF Automated Processing & Validation")

st.write("Processing PDFs and generating validation report...")

pdf_folder = "data"

results_list = []

# List all PDFs in dataset folder
pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]

progress = st.progress(0)

for idx, pdf_file in enumerate(pdf_files):
    pdf_path = os.path.join(pdf_folder, pdf_file)
    structured_content = process_pdf(pdf_path)
    results = run_baseline_models(structured_content)
    results_list.append({
        "filename": pdf_file,
        "results": results
    })
    progress.progress((idx + 1)/len(pdf_files))

# Generate report
generate_report(results_list, output_path="validation_report.xlsx")

st.success("Processing completed! Validation report saved as 'validation_report.xlsx'")
