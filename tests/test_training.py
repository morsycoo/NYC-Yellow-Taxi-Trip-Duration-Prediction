import pandas as pd

from src.training import train_linear_regression


def test_train_linear_regression():

    X = pd.DataFrame(
        {
            "distance": [1, 2, 3, 4],
        }
    )

    y = [2, 4, 6, 8]

    model = train_linear_regression(
        X,
        y,
    )

    predictions = model.predict(X)

    assert len(predictions) == len(y)