"""
inference.py
------------
Inference utilities for the NYC Yellow Taxi Trip Duration Prediction project.

This module provides reusable functions for:

- Loading the production pipeline
- Single prediction
- Batch prediction
"""

from __future__ import annotations

import joblib
import pandas as pd


def load_pipeline(model_path: str):
    """
    Load a serialized production pipeline.

    Parameters
    ----------
    model_path : str
        Path to the saved pipeline.

    Returns
    -------
    sklearn.pipeline.Pipeline
    """

    return joblib.load(model_path)


def predict(pipeline, data):
    """
    Generate predictions.

    Parameters
    ----------
    pipeline
        Trained production pipeline.

    data
        pandas DataFrame or compatible input.

    Returns
    -------
    numpy.ndarray
    """

    return pipeline.predict(data)


def predict_single(pipeline, sample: dict):
    """
    Predict a single sample.

    Parameters
    ----------
    pipeline
        Trained pipeline.

    sample : dict
        Input feature dictionary.

    Returns
    -------
    float
    """

    df = pd.DataFrame([sample])

    prediction = pipeline.predict(df)

    return float(prediction[0])


def predict_batch(pipeline, samples: list[dict]):
    """
    Predict multiple samples.

    Parameters
    ----------
    pipeline
        Trained pipeline.

    samples : list[dict]

    Returns
    -------
    list[float]
    """

    df = pd.DataFrame(samples)

    predictions = pipeline.predict(df)

    return predictions.tolist()