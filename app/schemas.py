from typing import Literal

from pydantic import BaseModel, Field, ConfigDict


class TripRequest(BaseModel):
    """
    Request schema for predicting NYC taxi trip duration.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "VendorID": 2,
                "passenger_count": 1,
                "trip_distance": 3.7,
                "pickup_hour": 15,
                "pickup_weekday": 2,
                "pickup_week": 12,
                "pickup_month": 3,
                "pickup_longitude": -73.98,
                "pickup_latitude": 40.76,
                "RateCodeID": 1
            }
        }
    )

    VendorID: Literal[1, 2] = Field(
        ...,
        description="Taxi vendor identifier."
    )

    passenger_count: int = Field(
        ...,
        ge=1,
        le=8,
        description="Number of passengers."
    )

    trip_distance: float = Field(
        ...,
        ge=0,
        description="Trip distance in miles."
    )

    pickup_hour: int = Field(
        ...,
        ge=0,
        le=23,
        description="Pickup hour (24-hour format)."
    )

    pickup_weekday: int = Field(
        ...,
        ge=0,
        le=6,
        description="Day of week (0=Monday, 6=Sunday)."
    )

    pickup_week: int = Field(
        ...,
        ge=1,
        le=53,
        description="Week number of the year."
    )

    pickup_month: int = Field(
        ...,
        ge=1,
        le=12,
        description="Pickup month."
    )

    pickup_longitude: float = Field(
        ...,
        ge=-180,
        le=180,
        description="Pickup longitude."
    )

    pickup_latitude: float = Field(
        ...,
        ge=-90,
        le=90,
        description="Pickup latitude."
    )

    RateCodeID: int = Field(
        ...,
        ge=1,
        le=6,
        description="Taxi rate code."
    )

class PredictionResponse(BaseModel):
    """
    Prediction response schema.
    """

    success: bool

    predicted_trip_duration: float

    unit: str

    model: str

    version: str

class HealthResponse(BaseModel):
    """
    Health check response.
    """

    status: str

    service: str

    version: str