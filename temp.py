from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/nearest")
def get_nearest(
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude")
):
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": lat,
        "lon": lon,
        "format": "json",
        "addressdetails": 1,
        "zoom": 16,  # Higher zoom for more details
    }
    headers = {
        "User-Agent": "kuwait-nearest-spot-api",
        "accept-language": "en"
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    address = data.get("address", {})
    result = {
        "famous_spot": address.get("attraction") or address.get("building") or address.get("amenity") or address.get("shop") or address.get("tourism") or address.get("leisure"),
        "road": address.get("road"),
        "city": address.get("city") or address.get("town"),
        "postcode": address.get("postcode"),
        "display_name": data.get("display_name"),
        "lat": data.get("lat"),
        "lon": data.get("lon"),
    }
    return result




