"""
validation_report.py
Generate a validation report for all PDFs.
"""

import pandas as pd
import os

def generate_report(results_list, output_path="validation_report.xlsx"):
    """
    results_list: list of dicts with {'filename':..., 'results':...}
    """
    report_data = []
    for item in results_list:
        row = {"filename": item["filename"]}
        row.update(item["results"])
        report_data.append(row)

    df = pd.DataFrame(report_data)
    df.to_excel(output_path, index=False)
    print(f"Validation report saved to {output_path}")
