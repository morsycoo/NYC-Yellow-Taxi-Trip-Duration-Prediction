"""
FastAPI application for NYC Taxi Trip Duration Prediction.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.inference import load_pipeline, predict_single

ARTIFACTS_DIR = Path("artifacts")
PIPELINE_PATH = ARTIFACTS_DIR / "production_pipeline.pkl"

app = FastAPI(
    title="NYC Taxi Trip Duration Prediction API",
    description="Predict taxi trip duration using a trained Random Forest Pipeline.",
    version="1.0.0",
)

pipeline = None

if PIPELINE_PATH.exists():
    pipeline = load_pipeline(PIPELINE_PATH)


class TripRequest(BaseModel):

    vendor_id: int = Field(..., example=2)
    passenger_count: int = Field(..., ge=1, example=2)

    pickup_longitude: float
    pickup_latitude: float

    dropoff_longitude: float
    dropoff_latitude: float

    pickup_month: int
    pickup_day: int
    pickup_hour: int
    pickup_weekday: int

    trip_distance: float


@app.get("/")
def root():

    return {
        "message": "NYC Taxi Trip Duration Prediction API",
        "status": "running",
    }


@app.get("/health")
def health():

    return {
        "status": "healthy",
    }


@app.post("/predict")
def predict(request: TripRequest):

    if pipeline is None:
        raise HTTPException(
            status_code=500,
            detail="Production pipeline not found.",
        )

    prediction = predict_single(
        pipeline,
        request.model_dump(),
    )

    return {
        "predicted_trip_duration": round(prediction, 2)
    }