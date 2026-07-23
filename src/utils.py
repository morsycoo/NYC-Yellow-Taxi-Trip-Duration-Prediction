"""
utils.py
---------
General utility functions for the NYC Yellow Taxi Trip Duration Prediction project.

This module contains reusable helper functions for:

- Reproducibility
- JSON serialization
- Directory management
- Logging configuration
"""

from __future__ import annotations

import json
import logging
import random
from pathlib import Path

import numpy as np


def set_random_seed(seed: int = 42) -> None:
    """
    Set random seed for reproducibility.

    Parameters
    ----------
    seed : int
        Random seed.
    """

    random.seed(seed)

    np.random.seed(seed)


def ensure_directory(path: str | Path) -> Path:
    """
    Create a directory if it does not already exist.

    Parameters
    ----------
    path : str | Path

    Returns
    -------
    pathlib.Path
    """

    directory = Path(path)

    directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    return directory


def save_json(data: dict, filepath: str | Path) -> None:
    """
    Save a dictionary as a JSON file.
    """

    filepath = Path(filepath)

    ensure_directory(filepath.parent)

    with filepath.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
        )


def load_json(filepath: str | Path) -> dict:
    """
    Load a JSON file.
    """

    filepath = Path(filepath)

    with filepath.open(
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


def configure_logging(level=logging.INFO):
    """
    Configure project logging.
    """

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    return logging.getLogger(__name__)