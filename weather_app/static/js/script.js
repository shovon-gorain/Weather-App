class WeatherApp {
    constructor() {
        this.currentBackground = '';
        this.init();
    }

    init() {
        this.bindEvents();
        this.loadLastSearch();
    }

    bindEvents() {
        const searchBtn = document.getElementById('searchBtn');
        const searchInput = document.getElementById('searchInput');

        searchBtn.addEventListener('click', () => this.searchWeather());
        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.searchWeather();
            }
        });
    }

    async searchWeather() {
        const city = document.getElementById('searchInput').value.trim();
        
        if (!city) {
            this.showError('Please enter a city name');
            return;
        }

        this.showLoading();
        this.hideError();
        this.hideWeather();

        try {
            const response = await fetch('/weather', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ city: city })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Failed to fetch weather data');
            }

            this.displayWeather(data);
            this.saveLastSearch(city);
            
        } catch (error) {
            this.showError(error.message);
        } finally {
            this.hideLoading();
        }
    }

    displayWeather(data) {
        this.updateBackground(data.background_image);
        this.updateCurrentWeather(data.location, data.current_weather);
        this.updateForecast(data.forecast);
        this.showWeather();
    }

    updateBackground(backgroundImage) {
        const app = document.querySelector('.weather-app');
        
        if (backgroundImage && backgroundImage.url) {
            app.style.backgroundImage = `url(${backgroundImage.url})`;
            this.updatePhotoCredit(backgroundImage);
        } else {
            app.style.backgroundImage = '';
            this.hidePhotoCredit();
        }
    }

    updatePhotoCredit(backgroundImage) {
        let credit = document.getElementById('photoCredit');
        
        if (!credit) {
            credit = document.createElement('div');
            credit.id = 'photoCredit';
            credit.className = 'photo-credit';
            document.querySelector('.container').appendChild(credit);
        }

        credit.innerHTML = `
            Photo by 
            <a href="${backgroundImage.photographer_url}?utm_source=weather_app&utm_medium=referral" target="_blank">
                ${backgroundImage.photographer}
            </a>
            on Unsplash
        `;
        credit.style.display = 'block';
    }

    hidePhotoCredit() {
        const credit = document.getElementById('photoCredit');
        if (credit) {
            credit.style.display = 'none';
        }
    }

    updateCurrentWeather(location, weather) {
        document.getElementById('locationName').textContent = location.name;
        document.getElementById('locationRegion').textContent = 
            `${location.region}, ${location.country}`;
        
        document.getElementById('temperature').textContent = 
            `${Math.round(weather.temperature)}°C`;
        document.getElementById('weatherDescription').textContent = weather.weather_text;
        
        // Update weather icon
        const iconUrl = this.getWeatherIconUrl(weather.weather_icon);
        document.getElementById('weatherIcon').src = iconUrl;
        document.getElementById('weatherIcon').alt = weather.weather_text;

        // Update details
        document.getElementById('realFeel').textContent = `${Math.round(weather.real_feel)}°C`;
        document.getElementById('humidity').textContent = `${weather.humidity}%`;
        document.getElementById('windSpeed').textContent = `${weather.wind_speed} km/h`;
        document.getElementById('windDirection').textContent = weather.wind_direction;
        document.getElementById('pressure').textContent = `${weather.pressure} hPa`;
        document.getElementById('uvIndex').textContent = weather.uv_index;
        document.getElementById('visibility').textContent = `${weather.visibility} km`;
    }

    updateForecast(forecast) {
        const forecastContainer = document.getElementById('forecastCards');
        forecastContainer.innerHTML = '';

        forecast.forEach(day => {
            const date = new Date(day.date).toLocaleDateString('en-US', {
                weekday: 'short',
                month: 'short',
                day: 'numeric'
            });

            const forecastCard = document.createElement('div');
            forecastCard.className = 'forecast-card fade-in';
            forecastCard.innerHTML = `
                <div class="forecast-date">${date}</div>
                <img src="${this.getWeatherIconUrl(day.day_icon)}" 
                     alt="${day.day_text}" 
                     class="weather-icon small">
                <div class="forecast-temps">
                    <span class="temp-high">${Math.round(day.max_temp)}°</span>
                    <span class="temp-low">${Math.round(day.min_temp)}°</span>
                </div>
                <div class="forecast-description">${day.day_text}</div>
            `;

            forecastContainer.appendChild(forecastCard);
        });
    }

    getWeatherIconUrl(iconNumber) {
        // AccuWeather icons - you can replace with your own icons or use AccuWeather's
        const iconMap = {
            1: '☀️', 2: '⛅', 3: '☁️', 4: '☁️', 5: '🌫️',
            6: '🌧️', 7: '🌨️', 8: '🌧️', 9: '🌧️', 10: '🌧️',
            11: '🌫️', 12: '🌧️', 13: '🌨️', 14: '🌨️', 15: '🌨️',
            // Add more mappings as needed
        };
        
        // For now, using emoji as placeholder
        return `https://developer.accuweather.com/sites/default/files/${iconNumber.toString().padStart(2, '0')}-s.png`;
    }

    showLoading() {
        document.getElementById('loading').style.display = 'block';
    }

    hideLoading() {
        document.getElementById('loading').style.display = 'none';
    }

    showWeather() {
        document.getElementById('weatherDisplay').style.display = 'block';
    }

    hideWeather() {
        document.getElementById('weatherDisplay').style.display = 'none';
    }

    showError(message) {
        const errorElement = document.getElementById('errorMessage');
        errorElement.textContent = message;
        errorElement.style.display = 'block';
    }

    hideError() {
        document.getElementById('errorMessage').style.display = 'none';
    }

    saveLastSearch(city) {
        localStorage.setItem('lastWeatherSearch', city);
    }

    loadLastSearch() {
        const lastSearch = localStorage.getItem('lastWeatherSearch');
        if (lastSearch) {
            document.getElementById('searchInput').value = lastSearch;
            // Optionally auto-search for last location
            // this.searchWeather();
        }
    }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new WeatherApp();
});

// Service Worker Registration for PWA capabilities
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}