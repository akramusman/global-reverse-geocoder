from fastapi import FastAPI, Query
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, or set your domain for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        "street_no": address.get("house_number") or "Not available",
        "boulevard": address.get("road") or "Not available",
        "block": address.get("suburb") or address.get("neighbourhood") or address.get("quarter") or address.get("block") or "Not available",
        "city": address.get("city") or address.get("town") or "Not available",
    }
    return result




