"""
preprocessing.py
----------------
Data preprocessing utilities for the NYC Yellow Taxi Trip Duration Prediction project.

This module contains reusable functions for:

- Data cleaning
- Feature selection
- Data type validation
- Missing value verification
- Feature/target separation
"""

from __future__ import annotations

import pandas as pd


def select_features(
    df: pd.DataFrame,
    target_column: str,
    drop_columns: list[str] | None = None,
):
    """
    Separate features and target.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe.

    target_column : str
        Target column.

    drop_columns : list[str], optional
        Leakage or unnecessary columns.

    Returns
    -------
    X : pd.DataFrame
    y : pd.Series
    """

    drop_columns = drop_columns or []

    X = df.drop(columns=[target_column] + drop_columns)

    y = df[target_column]

    return X, y


def validate_dataset(df: pd.DataFrame):
    """
    Perform basic data validation.

    Returns
    -------
    dict
    """

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
    }


def get_feature_types(df: pd.DataFrame):
    """
    Separate numerical and categorical features.
    """

    numerical = df.select_dtypes(include="number").columns.tolist()

    categorical = df.select_dtypes(
        exclude="number"
    ).columns.tolist()

    return numerical, categorical


def remove_columns(
    df: pd.DataFrame,
    columns: list[str],
):
    """
    Remove unnecessary columns.
    """

    return df.drop(columns=columns, errors="ignore")