import logging
import sys
from pathlib import Path

# Logs directory create karo
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

# Basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOGS_DIR / "nextgen_api.log"),  # File mein logs
        logging.StreamHandler(sys.stdout)  # Console pe bhi dikhao
    ]
)

# FastAPI-specific logger
logger = logging.getLogger("nextgen_api")