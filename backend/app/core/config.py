import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Path configurations
# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ML directory
ML_DIR = BASE_DIR / "ml-pipeline"

# Data directory
DATA_DIR = ML_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
# Model directory
MODELS_DIR = ML_DIR / "models"

DIRECTORIES = [
    ML_DIR,
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    MODELS_DIR
]

# API Configurations
CYBOTRADE_API_KEY = os.getenv("CYBOTRADE_API_KEY")
CYBOTRADE_ROOT_URL = "https://api.datasource.cybotrade.rs/"
CRYPTOQUANT_API_URL = "https://api.datasource.cybotrade.rs/cryptoquant"
REQUEST_LIMIT = 25000



def create_directories():
    for directory in DIRECTORIES:
        directory.mkdir(parents=True, exist_ok=True)
        
        
create_directories()