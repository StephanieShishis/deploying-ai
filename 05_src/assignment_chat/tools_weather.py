from langchain.tools import tool
import requests
 
@tool
def get_weather(city: str) -> str:
    """
    Provides the current weather for a city (no API key needed).
    """
    response = requests.get(f"https://wttr.in/{city}?format=3")
    return response.text