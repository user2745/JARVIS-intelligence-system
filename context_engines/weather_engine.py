import requests

class WeatherEngine:
    def run(self):
        try:
            response = requests.get("https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=London")
            weather = response.json()
            return {"weather": weather["current"]["condition"]["text"], "temperature": weather["current"]["temp_c"]}
        except Exception as e:
            return {"weather": "Unknown", "temperature": None}
