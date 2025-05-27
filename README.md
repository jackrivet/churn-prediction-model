# Customer Termination Risk Pipeline
An end-to-end churn risk prediction system built to support proactive outreach to at-risk school customers. The pipeline pulls SQL Server data, trains a neural network, calibrates predictions, explains model behavior, and generates visual + tabular reports that are automatically emailed.

## Workflow Overview
- Pulls real-time data from MS SQL Server
- Builds a neural network using TensorFlow with SMOTE + feature scaling
- Calibrates with Isotonic Regression
- Explains outputs with SHAP (summary, force, waterfall plots)
- Exports results and visualizations
- Sends a fully automated routine email to stakeholders
## Tech Stack
- **Python**: pandas, TensorFlow, pyodbc, matplotlib, shap, sklearn, imblearn
- **SQL Server**: Data source via pyodbc
- **Visualization**: SHAP, Matplotlib, Seaborn
- **Automation**: smtplib for email delivery

## How to Run
- Set up a `.env` file (example provided)
- Run `main.py` to execute the full workflow
- Note: This version excludes real credentials and data.
- **Evaluation Caveat:** 
This version of the model trains and tests on the same pulled dataset. It filters out terminated customers after scoring, which risks introducing leakage. In a future version, this will be addressed by scoring only on customers active at the time of inference and separating evaluation from calibration.
## Author
Jack Rivet – [LinkedIn](https://www.linkedin.com/in/jack-rivet-6a810a197)
