import os
import sys
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from data_prep import load_data
from model import run_model_pipeline
from explain import generate_shap_plots
from email_report import send_email_report

# -----------------------------
# Configuration 
# -----------------------------

QUERY_PATH = "sql/churn_query.sql"
OUTPUT_DIR = "sample_outputs"
SENDER_EMAIL = "your_email@example.com"
RECIPIENT_EMAIL = "recipient_email@example.com"
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD") 

def main():
    print("Starting churn prediction pipeline")
    df = load_data(QUERY_PATH)
    print("Training model...")
    model, iso_reg, X_test, y_test, calibrated, id_test = run_model_pipeline(df)
    print("Generating SHAP visualizations")
  
    explanations = generate_shap_plots(
        model,
        X_test.iloc[:100],
        group_patterns=[],  # Optional if not aggregating
        output_dir=OUTPUT_DIR
    )
  
    print("Sending report via email")
    send_email_report(
        attachments=list(explanations.values()),
        sender_email=SENDER_EMAIL,
        recipient_email=RECIPIENT_EMAIL,
        password=EMAIL_PASSWORD
    )
  
    print("Pipeline completed!")
  
if __name__ == "__main__":
    main()
