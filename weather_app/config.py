import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ACCUWEATHER_API_KEY = os.getenv('ACCUWEATHER_API_KEY')
    UNSPLASH_API_KEY = os.getenv('UNSPLASH_API_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    
    # AccuWeather API endpoints
    ACCUWEATHER_BASE_URL = "http://dataservice.accuweather.com"
    LOCATION_SEARCH_URL = "/locations/v1/cities/search"
    CURRENT_WEATHER_URL = "/currentconditions/v1/"
    FORECAST_URL = "/forecasts/v1/daily/5day/"
    
    # Unsplash API for background images
    UNSPLASH_BASE_URL = "https://api.unsplash.com"
    UNSPLASH_SEARCH_URL = "/search/photos"