import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class WeatherFetcher:
    def __init__(self, api_key: str):
        """
        Initialize WeatherFetcher with OpenWeatherMap API key.
        
        Get your free API key from: https://openweathermap.org/api
        """
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"
        
    def get_current_weather(self, city: str, country_code: str = "TW") -> Optional[Dict]:
        """
        Get current weather for a specific city.
        
        Args:
            city: City name (e.g., "Taipei", "Taichung", "Kaohsiung")
            country_code: Country code (default: "TW" for Taiwan)
            
        Returns:
            Dictionary with current weather data or None if error
        """
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q": f"{city},{country_code}",
                "appid": self.api_key,
                "units": "metric"  # Celsius
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            return {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "weather": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"],
                "timestamp": datetime.fromtimestamp(data["dt"]).strftime("%Y-%m-%d %H:%M:%S")
            }
            
        except requests.RequestException as e:
            print(f"Error fetching current weather: {e}")
            return None
        except KeyError as e:
            print(f"Error parsing weather data: {e}")
            return None
    
    def get_forecast(self, city: str, country_code: str = "TW", days: int = 10) -> Optional[List[Dict]]:
        """
        Get weather forecast for the next several days.
        
        Note: Free tier of OpenWeatherMap provides 5-day forecast.
        For 10+ days, you need a paid plan.
        
        Args:
            city: City name
            country_code: Country code (default: "TW")
            days: Number of days (max 5 for free tier)
            
        Returns:
            List of daily weather forecasts or None if error
        """
        try:
            url = f"{self.base_url}/forecast"
            params = {
                "q": f"{city},{country_code}",
                "appid": self.api_key,
                "units": "metric"
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            # Process forecast data (API returns 3-hour intervals)
            daily_forecasts = []
            current_date = None
            daily_temps = []
            daily_weather = []
            
            for item in data["list"][:days*8]:  # Approximate daily data
                forecast_date = datetime.fromtimestamp(item["dt"]).date()
                
                if current_date != forecast_date:
                    if current_date is not None:
                        # Save previous day's data
                        daily_forecasts.append({
                            "date": current_date.strftime("%Y-%m-%d"),
                            "avg_temp": round(sum(daily_temps) / len(daily_temps), 1),
                            "min_temp": min(daily_temps),
                            "max_temp": max(daily_temps),
                            "weather": max(set(daily_weather), key=daily_weather.count),
                            "city": data["city"]["name"]
                        })
                    
                    current_date = forecast_date
                    daily_temps = []
                    daily_weather = []
                
                daily_temps.append(item["main"]["temp"])
                daily_weather.append(item["weather"][0]["description"])
            
            # Add the last day
            if daily_temps:
                daily_forecasts.append({
                    "date": current_date.strftime("%Y-%m-%d"),
                    "avg_temp": round(sum(daily_temps) / len(daily_temps), 1),
                    "min_temp": min(daily_temps),
                    "max_temp": max(daily_temps),
                    "weather": max(set(daily_weather), key=daily_weather.count),
                    "city": data["city"]["name"]
                })
            
            return daily_forecasts[:days]
            
        except requests.RequestException as e:
            print(f"Error fetching forecast: {e}")
            return None
        except KeyError as e:
            print(f"Error parsing forecast data: {e}")
            return None

def get_taiwan_weather(city: str = "Taipei", api_key: str = None, forecast_days: int = 5) -> Dict:
    """
    Main function to get Taiwan weather data.
    
    Args:
        city: Taiwan city name (Taipei, Taichung, Kaohsiung, Tainan, etc.)
        api_key: Your OpenWeatherMap API key
        forecast_days: Number of forecast days (max 5 for free tier)
        
    Returns:
        Dictionary with current weather and forecast
    """
    if not api_key:
        return {"error": "API key is required. Get one from https://openweathermap.org/api"}
    
    weather = WeatherFetcher(api_key)
    
    # Get current weather
    current = weather.get_current_weather(city)
    if not current:
        return {"error": f"Could not fetch weather for {city}"}
    
    # Get forecast
    forecast = weather.get_forecast(city, days=forecast_days)
    if not forecast:
        return {"error": f"Could not fetch forecast for {city}"}
    
    return {
        "current_weather": current,
        "forecast": forecast,
        "summary": f"Current temperature in {current['city']}: {current['temperature']}°C ({current['weather']})"
    }

# Example usage
if __name__ == "__main__":
    # Replace with your actual API key
    API_KEY = "your_openweathermap_api_key_here"
    
    # Popular Taiwan cities
    taiwan_cities = ["Taipei", "Taichung", "Kaohsiung", "Tainan", "Hsinchu", "Keelung"]
    
    print("=== Taiwan Weather Report ===\n")
    
    for city in taiwan_cities[:3]:  # Show first 3 cities
        print(f"Weather for {city}:")
        result = get_taiwan_weather(city, API_KEY, forecast_days=5)
        
        if "error" in result:
            print(f"  Error: {result['error']}")
        else:
            print(f"  {result['summary']}")
            print(f"  Humidity: {result['current_weather']['humidity']}%")
            print(f"  5-day forecast available")
        print()
    
    # Example: Get detailed forecast for Taipei
    print("=== Detailed Taipei Forecast ===")
    taipei_weather = get_taiwan_weather("Taipei", API_KEY, forecast_days=5)
    
    if "forecast" in taipei_weather:
        for day in taipei_weather["forecast"]:
            print(f"{day['date']}: {day['min_temp']}°C - {day['max_temp']}°C, {day['weather']}")
