import shap
import numpy as np
import os
import matplotlib.pyplot as plt
from datetime import date

def generate_shap_plots(model, X_sample, group_patterns, output_dir='sample_outputs'):
    current_date = date.today()

    filtered_feature_names = X_sample.columns.tolist()
    filtered_X = np.nan_to_num(X_sample.astype(np.float32))

    explainer = shap.DeepExplainer(model, filtered_X)
    shap_values = explainer(filtered_X)
    shap_vals = shap_values.values if isinstance(shap_values, shap.Explanation) else shap_values[0]
  
    # SHAP summary plot
    plt.figure()
    shap.summary_plot(shap_vals, filtered_X, feature_names=filtered_feature_names, show=False)
    summary_path = os.path.join(output_dir, f"summary_plot_{current_date}.png")
    plt.savefig(summary_path, bbox_inches='tight')
    plt.close()
  
    # Waterfall plot for one sample
    sample_index = 0
  
    explanation = shap.Explanation(
        values=shap_vals[sample_index],
        base_values=explainer.expected_value[0],
        data=filtered_X[sample_index],
        feature_names=filtered_feature_names
    )
  
    shap.waterfall_plot(explanation, show=False)
    waterfall_path = os.path.join(output_dir, f"waterfall_plot_{current_date}.png")
    plt.savefig(waterfall_path, bbox_inches='tight')
    plt.close()
  
    # Save Force plot as HTML
    force_path = os.path.join(output_dir, f"force_plot_{current_date}.html")
    shap.save_html(force_path, shap.force_plot(
        explainer.expected_value[0],
        shap_vals[sample_index],
        filtered_X[sample_index],
        feature_names=filtered_feature_names,
        show=False
    ))
  
    return {
        "summary": summary_path,
        "waterfall": waterfall_path,
        "force": force_path
    }
