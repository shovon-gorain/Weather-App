import requests
from flask import current_app
import json

class WeatherAPI:
    def __init__(self):
        self.base_url = current_app.config['ACCUWEATHER_BASE_URL']
        self.api_key = current_app.config['ACCUWEATHER_API_KEY']
    
    def get_location_key(self, city_name):
        """Get location key for the city"""
        try:
            params = {
                'apikey': self.api_key,
                'q': city_name,
                'language': 'en-us'
            }
            
            response = requests.get(
                f"{self.base_url}{current_app.config['LOCATION_SEARCH_URL']}",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            
            locations = response.json()
            if locations:
                return {
                    'key': locations[0]['Key'],
                    'name': locations[0]['LocalizedName'],
                    'country': locations[0]['Country']['LocalizedName'],
                    'region': locations[0]['Region']['LocalizedName']
                }
            return None
        except requests.exceptions.RequestException as e:
            current_app.logger.error(f"Error fetching location: {e}")
            return None
    
    def get_current_weather(self, location_key):
        """Get current weather conditions"""
        try:
            params = {
                'apikey': self.api_key,
                'language': 'en-us',
                'details': True
            }
            
            response = requests.get(
                f"{self.base_url}{current_app.config['CURRENT_WEATHER_URL']}{location_key}",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()[0]
            
            return {
                'temperature': data['Temperature']['Metric']['Value'],
                'weather_text': data['WeatherText'],
                'weather_icon': data['WeatherIcon'],
                'is_day': data['IsDayTime'],
                'real_feel': data['RealFeelTemperature']['Metric']['Value'],
                'humidity': data['RelativeHumidity'],
                'wind_speed': data['Wind']['Speed']['Metric']['Value'],
                'wind_direction': data['Wind']['Direction']['Localized'],
                'pressure': data['Pressure']['Metric']['Value'],
                'uv_index': data['UVIndex'],
                'visibility': data['Visibility']['Metric']['Value']
            }
        except requests.exceptions.RequestException as e:
            current_app.logger.error(f"Error fetching current weather: {e}")
            return None
    
    def get_forecast(self, location_key):
        """Get 5-day weather forecast"""
        try:
            params = {
                'apikey': self.api_key,
                'language': 'en-us',
                'metric': True
            }
            
            response = requests.get(
                f"{self.base_url}{current_app.config['FORECAST_URL']}{location_key}",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            daily_forecasts = data['DailyForecasts']
            
            forecast = []
            for day in daily_forecasts:
                forecast.append({
                    'date': day['Date'],
                    'min_temp': day['Temperature']['Minimum']['Value'],
                    'max_temp': day['Temperature']['Maximum']['Value'],
                    'day_icon': day['Day']['Icon'],
                    'day_text': day['Day']['IconPhrase'],
                    'night_icon': day['Night']['Icon'],
                    'night_text': day['Night']['IconPhrase']
                })
            
            return forecast
        except requests.exceptions.RequestException as e:
            current_app.logger.error(f"Error fetching forecast: {e}")
            return None