# WeatherSphere - Advanced Weather Application

![WeatherSphere](https://img.shields.io/badge/WeatherSphere-Advanced%20Weather%20App-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![Flask](https://img.shields.io/badge/Flask-2.3.3-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

A modern, responsive weather application built with Flask that provides accurate weather forecasts with stunning visual backgrounds.

## 🌟 Features

### Core Features
- **Real-time Weather Data** - Powered by AccuWeather API
- **Dynamic Backgrounds** - Beautiful location-based images from Unsplash
- **5-Day Forecast** - Detailed weather predictions
- **Responsive Design** - Works perfectly on all devices
- **Modern UI/UX** - Smooth animations and professional styling

### Advanced Features
- 🔍 **Smart Search** with auto-suggestions
- 📱 **Progressive Web App** ready
- 💾 **Local Storage** for last search
- ⚡ **Performance Optimized** with lazy loading
- ♿ **Accessibility** focused design
- 🔒 **Secure** with proper error handling
- 📸 **Photo Credits** for background images

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd weather_app
   ```

2. **Create virtual environment (Recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get API Keys**

   **AccuWeather API:**
   - Visit [AccuWeather Developer Portal](https://developer.accuweather.com/)
   - Sign up for a free account
   - Create a new app in "My Apps" section
   - Copy your API Key

   **Unsplash API:**
   - Visit [Unsplash Developers](https://unsplash.com/developers)
   - Create an account (if needed)
   - Create a new application
   - Copy your Access Key

5. **Configure Environment**
   ```bash
   # Create .env file
   touch .env
   ```

   Add your API keys to `.env`:
   ```env
   # Weather App Configuration
   ACCUWEATHER_API_KEY=your_accuweather_api_key_here
   UNSPLASH_API_KEY=your_unsplash_access_key_here
   SECRET_KEY=generate_a_secure_random_key_here
   ```

   **Generate SECRET_KEY:**
   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

6. **Run the Application**
   ```bash
   python app.py
   ```

7. **Access the Application**
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
weather_app/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (create this)
├── .gitignore          # Git ignore rules
├── static/
│   ├── css/
│   │   └── style.css    # Main stylesheet
│   └── js/
│       └── script.js    # Frontend JavaScript
├── templates/
│   ├── base.html        # Base template
│   └── index.html       # Main page template
└── utils/
    ├── weather_api.py   # AccuWeather API integration
    └── image_api.py     # Unsplash API integration
```

## 🔧 Configuration

### Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| `ACCUWEATHER_API_KEY` | Your AccuWeather API key | Yes |
| `UNSPLASH_API_KEY` | Your Unsplash Access Key | Yes |
| `SECRET_KEY` | Flask secret key for security | Yes |

### API Limits
- **AccuWeather**: 50 calls/day (free tier)
- **Unsplash**: 50 requests/hour (free tier)

## 🎯 Usage

### Searching for Weather
1. Enter a city name in the search box
2. Click "Search" or press Enter
3. View current weather and 5-day forecast
4. Enjoy dynamic background images of the location

### Features Overview
- **Current Weather**: Temperature, humidity, wind speed, pressure, UV index
- **5-Day Forecast**: Daily highs/lows with weather conditions
- **Background Images**: Automatically updates based on location
- **Responsive Design**: Optimized for mobile and desktop

## 🛠️ Development

### Running in Development Mode
```bash
python app.py
```

### Running in Production
For production deployment, consider using:
```bash
gunicorn app:app
```

### API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main weather application |
| `/weather` | POST | Fetch weather data for a city |
| `/suggestions` | GET | Get city search suggestions |
| `/health` | GET | Health check endpoint |

## 🐛 Troubleshooting

### Common Issues

1. **"City not found" error**
   - Try different city names or spellings
   - Use popular city tags for testing
   - Check your AccuWeather API key

2. **"API limit exceeded"**
   - Wait for rate limit reset
   - Check your API usage in developer portals

3. **Background images not loading**
   - Verify Unsplash API key
   - Check network connectivity

4. **Application won't start**
   - Verify all dependencies are installed
   - Check .env file exists with proper keys
   - Ensure Python 3.8+ is installed

### Debug Mode
Enable debug mode by setting `debug=True` in `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

## 📱 Progressive Web App

The application is PWA-ready with:
- Service worker support
- Offline functionality (basic)
- Installable on mobile devices
- Fast loading times

## 🌐 Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 🔒 Security Features

- Environment variable protection
- API key security
- Input validation
- Error handling
- XSS protection
- CSRF protection

## 📊 Performance

- Lazy loading of images
- Optimized API calls
- CSS and JS minification ready
- Cache control headers

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 🙏 Acknowledgments

- **AccuWeather** for reliable weather data
- **Unsplash** for beautiful background images
- **Flask** community for excellent documentation
- **Contributors** who help improve this project

## 📞 Support

If you encounter any issues:

1. Check the troubleshooting section above
2. Verify your API keys are correct
3. Ensure all dependencies are installed
4. Check the browser console for errors

For additional help, create an issue in the project repository.
