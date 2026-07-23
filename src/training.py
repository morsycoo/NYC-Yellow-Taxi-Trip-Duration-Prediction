"""
training.py
-----------
Model training utilities for the NYC Yellow Taxi Trip Duration Prediction project.

This module contains reusable functions for:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Model Saving
"""

from __future__ import annotations

import joblib

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


def train_linear_regression(X_train, y_train):
    """
    Train a Linear Regression model.
    """

    model = LinearRegression()

    model.fit(X_train, y_train)

    return model


def train_decision_tree(
    X_train,
    y_train,
    max_depth=None,
    min_samples_split=2,
    random_state=42,
):
    """
    Train a Decision Tree Regressor.
    """

    model = DecisionTreeRegressor(
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=random_state,
    )

    model.fit(X_train, y_train)

    return model


def train_random_forest(
    X_train,
    y_train,
    n_estimators=200,
    max_depth=10,
    min_samples_split=5,
    random_state=42,
):
    """
    Train a Random Forest Regressor.
    """

    model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=random_state,
        n_jobs=-1,
    )

    model.fit(X_train, y_train)

    return model


def save_model(model, filepath):
    """
    Save a trained model using Joblib.
    """

    joblib.dump(model, filepath)


def load_model(filepath):
    """
    Load a previously saved model.
    """

    return joblib.load(filepath)