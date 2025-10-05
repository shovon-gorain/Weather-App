from flask import Flask, render_template, request, jsonify
from config import Config
from utils.weather_api import WeatherAPI
from utils.image_api import ImageAPI
import json
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

weather_api = WeatherAPI()
image_api = ImageAPI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    try:
        city_name = request.json.get('city', '').strip()
        
        if not city_name:
            return jsonify({'error': 'City name is required'}), 400
        
        # Get location information
        location = weather_api.get_location_key(city_name)
        if not location:
            return jsonify({'error': 'City not found'}), 404
        
        # Get current weather
        current_weather = weather_api.get_current_weather(location['key'])
        if not current_weather:
            return jsonify({'error': 'Weather data not available'}), 500
        
        # Get forecast
        forecast = weather_api.get_forecast(location['key'])
        
        # Get background image
        background_image = image_api.get_city_image(city_name)
        
        response_data = {
            'location': location,
            'current_weather': current_weather,
            'forecast': forecast,
            'background_image': background_image,
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(response_data)
    
    except Exception as e:
        app.logger.error(f"Error in get_weather: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)