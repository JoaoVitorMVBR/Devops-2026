import openmeteo_requests
import requests_cache
from retry_requests import retry
import numpy as np


# Setup the Open-Meteo API client with cache and retry on fail
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# API parameters
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": -19.92,
    "longitude": -43.94,
    "current_weather": "true",
    "hourly": "temperature_2m",
    "timezone": "America/Sao_Paulo" # Ajusta o horário para o local
}

# Make the API call
responses = openmeteo.weather_api(url, params=params)

# Process responses
response = responses[0]
print(f"Coordinates: {response.Latitude()}°N, {response.Longitude()}°E")
print(f"Timezone: {response.Timezone()}")

# Extract hourly data
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

print(f"\nHourly temperature forecast:")
for i in range(min(24, len(hourly_temperature_2m))):  # Print first 24 hours
    print(f"Hour {i}: {hourly_temperature_2m[i]:.1f}°C")

