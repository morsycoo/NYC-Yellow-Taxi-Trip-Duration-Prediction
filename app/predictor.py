"""
Prediction Module

This module is responsible for:

1. Loading the production pipeline.
2. Running inference.
3. Returning prediction results.
"""

from pathlib import Path

import joblib
import pandas as pd

from app.logger import logger


# ============================================================
# Project Paths
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODELS_DIR = PROJECT_ROOT / "models"

PIPELINE_PATH = MODELS_DIR / "production_pipeline.pkl"


# ============================================================
# Load Production Pipeline
# ============================================================

pipeline = None

try:

    pipeline = joblib.load(PIPELINE_PATH)

    logger.info(
        "Production pipeline loaded successfully."
    )

except Exception:

    logger.exception(
        "Failed to load production pipeline."
    )


# ============================================================
# Prediction Function
# ============================================================

def predict_trip_duration(data: dict) -> float:
    """
    Predict NYC taxi trip duration.

    Parameters
    ----------
    data : dict
        Input features.

    Returns
    -------
    float
        Predicted trip duration in minutes.
    """

    if pipeline is None:

        logger.error(
            "Prediction attempted before pipeline was loaded."
        )

        raise RuntimeError(
            "Production pipeline is unavailable."
        )

    try:

        input_df = pd.DataFrame([data])

        prediction = pipeline.predict(input_df)

        logger.info(
            "Prediction completed successfully."
        )

        return float(prediction[0])

    except Exception:

        logger.exception(
            "Prediction failed."
        )

        raise