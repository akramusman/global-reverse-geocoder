from typing import List
import requests

class Locator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.example.com/locations"  # Replace with actual API endpoint

    def find_nearest_spot(self, lat: float, lon: float) -> dict:
        params = {
            'lat': lat,
            'lon': lon,
            'api_key': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Assuming the API returns JSON data