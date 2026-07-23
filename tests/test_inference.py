import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

from src.inference import predict


def test_predict():

    X = pd.DataFrame(
        {
            "distance": [1, 2, 3],
        }
    )

    y = [2, 4, 6]

    pipeline = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("model", LinearRegression()),
        ]
    )

    pipeline.fit(X, y)

    predictions = predict(
        pipeline,
        X,
    )

    assert len(predictions) == 3