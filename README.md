# predictive_analytics
AI-Powered Real Estate Analytics Platform

This repository contains an early-stage Prophecy AI backend for dataset acquisition, cleaning, and exploratory data analysis.

## Structure

- `backend/`
  - `app/` - FastAPI application code
  - `app/data/` - data loading and dataset storage
  - `app/services/` - data inspection and stats services
  - `notebooks/` - Jupyter notebooks for data collection and EDA
  - `requirements.txt` - Python dependencies
  - `README.md` - backend usage notes

## Getting Started

1. Change into the backend directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the API server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Notes

- The FastAPI backend downloads the California Housing dataset automatically if it is not already present.
- Exploratory notebooks are stored in `backend/notebooks/`.
