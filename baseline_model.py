"""
baseline_model.py
Run structured content through pre-existing baseline models.
"""

# Example: simple placeholder baseline model
# Replace with your actual baseline ML / rule-based models

def run_baseline_models(structured_content):
    """
    structured_content: dict with 'text' and 'tables'
    Return model results as a dict.
    """
    results = {}

    # Example text-based check
    if len(structured_content["text"]) > 0:
        results["text_present"] = True
    else:
        results["text_present"] = False

    # Example table-based check
    if len(structured_content["tables"]) > 0:
        results["tables_count"] = len(structured_content["tables"])
    else:
        results["tables_count"] = 0

    # Add more baseline model logic here

    return results
