# Weather Forecast API – Backend

A FastAPI-based backend service that provides weekly weather forecasts and solar energy production estimates based on geographic coordinates.

## Functionality

- Fetches weather data from **Open-Meteo**
- Computes:
  - Min/Max temperatures
  - Average sun exposure and pressure
  - Weekly energy production summary
- Returns structured data via clean REST endpoints

## Endpoints

- `GET /weather?lat={lat}&lon={lon}`  
  → Returns daily weather forecasts and energy estimates

- `GET /summary?lat={lat}&lon={lon}`  
  → Returns a weekly summary of atmospheric data and weather description

## Tech Stack

- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [Requests](https://pypi.org/project/requests/)
- [Uvicorn](https://www.uvicorn.org/) (for local server)

## Run Locally

```bash
# 1. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the development server
uvicorn main:app --reload
```

Once running, access the API at `http://localhost:8000`.

Swagger docs available at `http://localhost:8000/docs`.


## Related

This backend works with the companion [weather frontend](https://github.com/zacky111/weather-frontend).
