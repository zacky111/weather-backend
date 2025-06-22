from fastapi import HTTPException, APIRouter
import httpx

from src.func_endp_weather import calc_exp_generated_energy
from src.func_endp_summary import calc_mean_press, calc_mean_exposition, summary_weather


#bash: fastapi dev main.py
router = APIRouter()
@router.get("/weather")
async def get_weather(lat: float = 52.23, lon: float = 21.01):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&forecast_days=7"
        "&daily=temperature_2m_max,temperature_2m_min,weather_code,daylight_duration"
        "&timezone=Europe%2FWarsaw"
    )
    try:
        async with httpx.AsyncClient() as client:
            response_meteo_api = await client.get(url)
            response_meteo_api.raise_for_status()  # rzuca wyjątek dla błędów 4xx/5xx
            data_meteo_api = response_meteo_api.json()

            daily = data_meteo_api["daily"]
            result = []
            for date, t_max, t_min, weather_code, daylight_duration in zip(
                daily["time"], daily["temperature_2m_max"], daily["temperature_2m_min"], daily["weather_code"], daily["daylight_duration"]
            ):
                result.append({
                    "date": date,
                    "temp_max": t_max,
                    "temp_min": t_min,
                    "weather_code": weather_code,
                    "expected_generated_energy": calc_exp_generated_energy(daylight_duration)
                })

            return result

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=502, detail=f"Błąd API: {e.response.status_code}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/summary")

## endpoint for summary of week
## expected output:
## - mean value of pressure in coming week
## - mean value of time exposition in coming week
## - extreme values of temperature over the coming week
## - summary of weather - whether it'll rain or not

async def get_summary(lat: float = 52.23, lon: float = 21.01):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&forecast_days=7"
        "&daily=temperature_2m_max,temperature_2m_min,weather_code,daylight_duration"
        "&hourly=surface_pressure"
        "&timezone=Europe%2FWarsaw"
    )
    try:
        async with httpx.AsyncClient() as client:
            response_meteo_api = await client.get(url)
            response_meteo_api.raise_for_status() 
            data_meteo_api = response_meteo_api.json()

            daily=data_meteo_api["daily"]
            hourly=data_meteo_api["hourly"]


            result=[]

            result.append({
                "mean_press":calc_mean_press(hourly["surface_pressure"]),
                "mean_exposition":calc_mean_exposition(daily["daylight_duration"]),
                "min_temp": min(daily["temperature_2m_min"]),
                "max_temp": max(daily["temperature_2m_max"]),
                "summary": summary_weather(daily["weather_code"])
                })

            return result

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=502, detail=f"Błąd API: {e.response.status_code}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))