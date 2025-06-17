# 🌤️ Taiwan Weather Parser

A comprehensive Python weather client for fetching real-time weather data and forecasts for Taiwan cities using the OpenWeatherMap API.

## ✨ Features

- **🌡️ Current Weather**: Real-time temperature, humidity, pressure, and conditions
- **📅 5-Day Forecasts**: Daily weather predictions with min/max temperatures
- **🏙️ Taiwan Cities**: Optimized for Taiwan locations (Taipei, Taichung, Kaohsiung, etc.)
- **📊 Smart Processing**: Converts 3-hour API intervals into daily summaries
- **🛡️ Error Handling**: Robust error handling for API failures and data parsing
- **🔑 API Integration**: Uses OpenWeatherMap's reliable weather service

## 🚀 Installation

```bash
# Navigate to the weather parser directory
cd weather-parser

# Install required dependencies
pip install -r requirements.txt

# Or install manually
pip install requests
```

## 🔑 API Setup

1. **Get a free API key** from [OpenWeatherMap](https://openweathermap.org/api)
2. **Sign up** for a free account
3. **Copy your API key** from your account dashboard
4. **Replace the placeholder** in the code with your actual API key

```python
API_KEY = "your_actual_api_key_here"  # Replace this!
```

## 📖 Usage

### Quick Start

```python
from src.weather import get_taiwan_weather

# Get weather for Taipei (requires API key)
result = get_taiwan_weather("Taipei", api_key="your_api_key", forecast_days=5)

if "error" not in result:
    print(result["summary"])
    # Output: Current temperature in Taipei: 26.5°C (scattered clouds)
else:
    print(result["error"])
```

### Detailed Usage

```python
from src.weather import WeatherFetcher

# Initialize the weather client
weather = WeatherFetcher("your_api_key")

# Get current weather
current = weather.get_current_weather("Taipei")
print(f"Temperature: {current['temperature']}°C")
print(f"Feels like: {current['feels_like']}°C")
print(f"Humidity: {current['humidity']}%")
print(f"Weather: {current['weather']}")

# Get 5-day forecast
forecast = weather.get_forecast("Taipei", days=5)
for day in forecast:
    print(f"{day['date']}: {day['min_temp']}°C - {day['max_temp']}°C")
```

### Multiple Cities

```python
taiwan_cities = ["Taipei", "Taichung", "Kaohsiung", "Tainan", "Hsinchu"]

for city in taiwan_cities:
    result = get_taiwan_weather(city, API_KEY)
    if "error" not in result:
        weather = result["current_weather"]
        print(f"{city}: {weather['temperature']}°C, {weather['weather']}")
```

## 🏙️ Supported Taiwan Cities

The parser works with all major Taiwan cities:

- **Taipei** (台北) - Capital city
- **New Taipei** (新北) - Metropolitan area
- **Taoyuan** (桃園) - Airport city
- **Taichung** (台中) - Central Taiwan
- **Tainan** (台南) - Historic city
- **Kaohsiung** (高雄) - Southern port city
- **Hsinchu** (新竹) - Tech hub
- **Keelung** (基隆) - Northern port
- **Chiayi** (嘉義) - Central-south
- **Changhua** (彰化) - Central coast

## 📊 Data Structure

### Current Weather Response

```json
{
  "city": "Taipei",
  "country": "TW",
  "temperature": 26.5,
  "feels_like": 29.2,
  "humidity": 78,
  "pressure": 1013,
  "weather": "scattered clouds",
  "wind_speed": 3.2,
  "timestamp": "2025-06-17 14:30:00"
}
```

### Forecast Response

```json
{
  "date": "2025-06-18",
  "avg_temp": 27.3,
  "min_temp": 23.1,
  "max_temp": 31.5,
  "weather": "partly cloudy",
  "city": "Taipei"
}
```

### Complete Response Format

```json
{
  "current_weather": { /* current weather object */ },
  "forecast": [ /* array of daily forecasts */ ],
  "summary": "Current temperature in Taipei: 26.5°C (scattered clouds)"
}
```

## 🏃‍♂️ Running the Examples

```bash
# Run the main script with examples
python src/weather.py

# Run with your API key (set it in the code first)
python src/weather.py
```

### Sample Output

```
=== Taiwan Weather Report ===

Weather for Taipei:
  Current temperature in Taipei: 26.5°C (scattered clouds)
  Humidity: 78%
  5-day forecast available

Weather for Taichung:
  Current temperature in Taichung: 28.1°C (clear sky)
  Humidity: 65%
  5-day forecast available

=== Detailed Taipei Forecast ===
2025-06-17: 23.1°C - 31.5°C, partly cloudy
2025-06-18: 24.2°C - 30.8°C, light rain
2025-06-19: 22.9°C - 29.4°C, scattered clouds
2025-06-20: 23.7°C - 31.2°C, clear sky
2025-06-21: 25.1°C - 32.1°C, few clouds
```

## 🧪 Development Status

**Current Status**: ✅ Production Ready

### ✅ Completed Features
- [x] OpenWeatherMap API integration
- [x] Current weather fetching
- [x] 5-day weather forecasts
- [x] Taiwan cities optimization
- [x] Daily forecast aggregation
- [x] Error handling and validation
- [x] Multiple city support
- [x] Comprehensive examples

### 🔮 Planned Enhancements
- [ ] Weather alerts and warnings
- [ ] Historical weather data
- [ ] Weather maps integration
- [ ] Air quality data
- [ ] CLI interface
- [ ] Data export (CSV/JSON)
- [ ] Caching for API rate limits
- [ ] Weather visualization charts

## 🔧 API Reference

### `WeatherFetcher`

#### Constructor
```python
WeatherFetcher(api_key: str)
```

#### Methods

- **`get_current_weather(city: str, country_code: str = "TW") -> Optional[Dict]`**
  - Fetches current weather for a specific city
  - Returns detailed weather data or None if error

- **`get_forecast(city: str, country_code: str = "TW", days: int = 5) -> Optional[List[Dict]]`**
  - Fetches weather forecast for specified days
  - Processes 3-hour intervals into daily summaries
  - Free tier supports up to 5 days

### `get_taiwan_weather(city: str, api_key: str, forecast_days: int = 5) -> Dict`**
- Main convenience function for Taiwan weather
- Returns combined current weather and forecast data

## 📋 Requirements

- **Python 3.7+**
- **requests** library
- **OpenWeatherMap API key** (free tier available)

### API Limitations

- **Free Tier**: 1,000 calls/day, 5-day forecast
- **Paid Tiers**: More calls, 16-day forecast, historical data
- **Rate Limits**: 60 calls/minute maximum

## ⚠️ Important Notes

1. **API Key Security**: Never commit your API key to version control
2. **Rate Limits**: Free tier has daily limits - cache results when possible
3. **Error Handling**: Always check for errors in the response
4. **Units**: Temperature returned in Celsius (metric units)

## 🛡️ Error Handling

The code handles several error scenarios:

```python
# API key missing
{"error": "API key is required. Get one from https://openweathermap.org/api"}

# City not found
{"error": "Could not fetch weather for InvalidCity"}

# Network issues
# Prints: "Error fetching current weather: [specific error]"

# Data parsing issues  
# Prints: "Error parsing weather data: [specific error]"
```

## 🔗 Useful Links

- [OpenWeatherMap API Documentation](https://openweathermap.org/api)
- [Get Free API Key](https://openweathermap.org/appid)
- [API Response Examples](https://openweathermap.org/current)
- [Forecast API Details](https://openweathermap.org/forecast5)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Add your API key to test locally (don't commit it!)
4. Make your changes and test with real API calls
5. Commit your changes: `git commit -am 'Add new feature'`
6. Push to the branch: `git push origin feature/new-feature`
7. Submit a pull request

## 📄 License

MIT License - see the main repository for details.

---

*Part of the [experiments repository](../README.md)*