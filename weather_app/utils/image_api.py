import requests
from flask import current_app
import random

class ImageAPI:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
    
    def init_app(self, app):
        self.app = app
        self.base_url = app.config['UNSPLASH_BASE_URL']
        self.api_key = app.config['UNSPLASH_API_KEY']
    
    def get_city_image(self, city_name):
        """Get random background image for the city"""
        try:
            headers = {
                'Authorization': f'Client-ID {self.api_key}'
            }
            
            params = {
                'query': city_name,
                'orientation': 'landscape',
                'per_page': 20
            }
            
            response = requests.get(
                f"{self.base_url}{self.app.config['UNSPLASH_SEARCH_URL']}",
                headers=headers,
                params=params,
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            if data['results']:
                # Select a random image from the results
                image = random.choice(data['results'])
                return {
                    'url': image['urls']['regular'],
                    'photographer': image['user']['name'],
                    'photographer_url': image['user']['links']['html']
                }
            return None
        except requests.exceptions.RequestException as e:
            self.app.logger.error(f"Error fetching image: {e}")
            return None