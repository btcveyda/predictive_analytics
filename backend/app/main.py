from pathlib import Path

from fastapi import FastAPI

from app.data.clean_housing import clean_dataset
from app.data.load_housing import load_dataset
from app.services.stats import dataset_stats

app = FastAPI(title="Prophecy AI API")

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
RAW_DATA_PATH = DATA_DIR / "housing.csv"
CLEAN_DATA_PATH = DATA_DIR / "housing_clean.csv"


@app.on_event("startup")
def startup_event():
    if not RAW_DATA_PATH.exists():
        load_dataset(RAW_DATA_PATH)
    if not CLEAN_DATA_PATH.exists():
        clean_dataset(RAW_DATA_PATH, CLEAN_DATA_PATH)


@app.get("/")
def home():
    return {"message": "Prophecy AI API"}


@app.get("/stats")
def stats():
    return dataset_stats(CLEAN_DATA_PATH)
