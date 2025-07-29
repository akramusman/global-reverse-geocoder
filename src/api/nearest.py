from fastapi import APIRouter, Query
from services.locator import Locator
from types.spot import Spot

router = APIRouter()
locator = Locator()

@router.get("/nearest", response_model=Spot)
def find_nearest_spot(lat: float = Query(...), lon: float = Query(...)):
    return locator.find_nearest(lat, lon)