from fastapi import FastAPI

from app.schemas import (
    TripRequest,
    PredictionResponse,
    HealthResponse
)

from fastapi import FastAPI, HTTPException
from app.predictor import predict_trip_duration
from app.logger import logger


# ============================================================
# FastAPI Application
# ============================================================

app = FastAPI(

    title="NYC Taxi Trip Duration Prediction API",

    summary=(
        "Production-ready REST API for predicting NYC taxi trip duration."
    ),

    description="""
## Overview

This API predicts the duration of NYC Yellow Taxi trips using a trained
Random Forest Regression model packaged inside a Scikit-learn Pipeline.

### Features

- Input validation using Pydantic
- Production Pipeline
- Health Check Endpoint
- Logging
- Error Handling
- Interactive Swagger Documentation

### Model

Random Forest Regressor

### Framework

FastAPI
""",

    version="1.0.0",

    contact={

        "name": "Mahmoud Morsy",

        "url": "https://github.com/morsycoo"

    },

    license_info={

        "name": "MIT License"

    }

)


# ============================================================
# Startup Event
# ============================================================

@app.on_event("startup")
def startup_event():

    logger.info(
        "NYC Taxi Prediction API started successfully."
    )


# ============================================================
# Shutdown Event
# ============================================================

@app.on_event("shutdown")
def shutdown_event():

    logger.info(
        "NYC Taxi Prediction API stopped."
    )


# ============================================================
# Root Endpoint
# ============================================================

@app.get(

    "/",

    tags=["Root"],

    summary="Root Endpoint",

    description="Returns basic API information."

)
def root():

    logger.info("Root endpoint requested.")

    return {

        "message": "Welcome to the NYC Taxi Trip Duration Prediction API.",

        "version": "1.0.0",

        "documentation": "/docs"

    }


# ============================================================
# Health Check Endpoint
# ============================================================

@app.get(

    "/health",

    response_model=HealthResponse,

    tags=["Health"],

    summary="Health Check",

    description="Checks whether the prediction service is healthy."

)


# ============================================================
# Prediction Endpoint
# ============================================================

@app.post(

    "/predict",

    response_model=PredictionResponse,

    tags=["Prediction"],

    summary="Predict Trip Duration",

    description="""
Predict the duration of an NYC taxi trip.
""",

    responses={

        200:{

            "description":"Prediction generated successfully."

        },

        422:{

            "description":"Validation Error."

        },

        500:{

            "description":"Internal Server Error."

        }

    }

)
def predict_trip_duration_endpoint(request: TripRequest):

    try:

        prediction = predict_trip_duration(request.dict())

        response = PredictionResponse(

            success=True,

            predicted_trip_duration=prediction,

            unit="minutes",

            model="Random Forest Regressor",

            version="1.0.0"

        )

        logger.info(
            "Prediction endpoint completed successfully."
        )

        return response

    except Exception as e:

        logger.exception(
            "Prediction endpoint failed."
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )