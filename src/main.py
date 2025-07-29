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
        "zoom": 16,
    }
    headers = {
        "User-Agent": "kuwait-nearest-spot-api",
        "accept-language": "en"
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    address = data.get("address", {})
    result = {
        "street_no": address.get("house_number") or "",
        "boulevard": address.get("road") or "",
        "block": address.get("suburb") or address.get("neighbourhood") or address.get("quarter") or address.get("block") or "",
        "city": address.get("city") or address.get("town") or "",
    }
    return result




