import random

def generate_weather_data():
    weather_conditions = ["Sunny", "Rainy", "Cloudy", "Stormy"]
    return {"weather": random.choice(weather_conditions)}

def generate_system_data():
    return {"cpu_usage": random.randint(10, 100), "memory_usage": random.randint(10, 100)}
