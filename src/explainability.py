"""
explainability.py
-----------------
Model explainability and visualization utilities.

This module provides reusable functions for:

- Feature Importance
- SHAP Explainability
- Residual Analysis
- Prediction Error Distribution
- Actual vs Predicted Visualization
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
import shap


def plot_feature_importance(
    model,
    feature_names,
    top_n=20,
):
    """
    Plot the top N feature importances.
    """

    importance = (
        pd.Series(
            model.feature_importances_,
            index=feature_names,
        )
        .sort_values(ascending=False)
        .head(top_n)
    )

    plt.figure(figsize=(10, 6))

    importance.plot(kind="barh")

    plt.gca().invert_yaxis()

    plt.title("Top Feature Importances")

    plt.xlabel("Importance")

    plt.tight_layout()

    plt.show()


def shap_summary_plot(
    model,
    X,
):
    """
    Generate SHAP summary plot.
    """

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X)

    shap.summary_plot(
        shap_values,
        X,
    )


def shap_beeswarm_plot(
    model,
    X,
):
    """
    Generate SHAP beeswarm plot.
    """

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X)

    shap.plots.beeswarm(shap_values)


def residual_plot(
    y_true,
    predictions,
):
    """
    Plot residuals.
    """

    residuals = y_true - predictions

    plt.figure(figsize=(8, 6))

    plt.scatter(
        predictions,
        residuals,
        alpha=0.4,
    )

    plt.axhline(
        0,
        linestyle="--",
    )

    plt.xlabel("Predicted")

    plt.ylabel("Residual")

    plt.title("Residual Plot")

    plt.tight_layout()

    plt.show()


def prediction_error_distribution(
    y_true,
    predictions,
):
    """
    Plot prediction error histogram.
    """

    errors = y_true - predictions

    plt.figure(figsize=(8, 6))

    plt.hist(
        errors,
        bins=40,
    )

    plt.title("Prediction Error Distribution")

    plt.xlabel("Prediction Error")

    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.show()


def actual_vs_predicted(
    y_true,
    predictions,
):
    """
    Plot actual vs predicted values.
    """

    plt.figure(figsize=(7, 7))

    plt.scatter(
        y_true,
        predictions,
        alpha=0.3,
    )

    plt.plot(
        [
            y_true.min(),
            y_true.max(),
        ],
        [
            y_true.min(),
            y_true.max(),
        ],
        linestyle="--",
    )

    plt.xlabel("Actual")

    plt.ylabel("Predicted")

    plt.title("Actual vs Predicted")

    plt.tight_layout()

    plt.show()