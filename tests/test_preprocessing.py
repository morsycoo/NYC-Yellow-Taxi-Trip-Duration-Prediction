import pandas as pd

from src.preprocessing import (
    select_features,
    validate_dataset,
)


def test_select_features():

    df = pd.DataFrame(
        {
            "distance": [1.5, 2.0],
            "passenger_count": [1, 2],
            "trip_duration": [300, 420],
        }
    )

    X, y = select_features(
        df,
        target_column="trip_duration",
    )

    assert "trip_duration" not in X.columns
    assert len(X.columns) == 2
    assert len(y) == 2


def test_validate_dataset():

    df = pd.DataFrame(
        {
            "a": [1, 2],
            "b": [3, 4],
        }
    )

    report = validate_dataset(df)

    assert report["rows"] == 2
    assert report["columns"] == 2
    assert report["missing_values"] == 0
    assert report["duplicate_rows"] == 0