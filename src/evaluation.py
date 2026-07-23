"""
evaluation.py
-------------
Model evaluation utilities for the NYC Yellow Taxi Trip Duration Prediction project.
"""

from __future__ import annotations

import time

import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


def evaluate_model(model, X_test, y_test):
    """
    Evaluate a regression model.
    """

    start = time.perf_counter()

    predictions = model.predict(X_test)

    inference_time = time.perf_counter() - start

    mae = mean_absolute_error(y_test, predictions)

    rmse = mean_squared_error(
        y_test,
        predictions,
        squared=False,
    )

    r2 = r2_score(
        y_test,
        predictions,
    )

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R²": r2,
        "Inference Time (sec)": inference_time,
    }


def benchmark_model(
    model_name,
    model,
    X_test,
    y_test,
):
    """
    Evaluate a model and return a benchmark row.
    """

    metrics = evaluate_model(
        model,
        X_test,
        y_test,
    )

    return {
        "Model": model_name,
        **metrics,
    }


def benchmark_dataframe(results):
    """
    Create a benchmark DataFrame.
    """

    df = pd.DataFrame(results)

    df = df.sort_values(
        by="R²",
        ascending=False,
    ).reset_index(drop=True)

    return df