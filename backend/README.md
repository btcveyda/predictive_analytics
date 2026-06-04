# Prophecy AI Backend

This backend serves the California Housing dataset and exposes dataset statistics via FastAPI.

## Setup

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app from the `backend/` folder:
   ```bash
   uvicorn app.main:app --reload
   ```

## Endpoints

- `GET /` - health check
- `GET /stats` - dataset statistics

## Notes

- The backend automatically downloads the California Housing dataset on startup if `housing.csv` does not exist.
- The dataset is saved to `backend/app/data/housing.csv`.
