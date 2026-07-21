from pathlib import Path
import logging


# ============================================================
# Project Paths
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

LOGS_DIR = PROJECT_ROOT / "logs"

LOGS_DIR.mkdir(exist_ok=True)

LOG_FILE = LOGS_DIR / "api.log"


# ============================================================
# Create Logger
# ============================================================

logger = logging.getLogger("NYC_Taxi_API")

logger.setLevel(logging.INFO)


# Prevent duplicated logs
logger.propagate = False


# Avoid duplicate handlers
if not logger.handlers:

    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)s | %(message)s"

    )

    file_handler = logging.FileHandler(LOG_FILE)

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.addHandler(console_handler)