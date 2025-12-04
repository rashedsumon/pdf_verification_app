"""
pdf_processor.py
Extract structured content from PDF files.
"""

import os
import pdfplumber  # or PyPDF2, Camelot for tables
import pandas as pd

def extract_text(pdf_path):
    """Extract text from PDF."""
    text_content = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text_content += page.extract_text() or ""
    return text_content

def extract_tables(pdf_path):
    """Extract tables from PDF as pandas DataFrames."""
    tables_list = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table[1:], columns=table[0])
                tables_list.append(df)
    return tables_list

def process_pdf(pdf_path):
    """Return structured content from a PDF."""
    text = extract_text(pdf_path)
    tables = extract_tables(pdf_path)
    return {
        "text": text,
        "tables": tables
    }
