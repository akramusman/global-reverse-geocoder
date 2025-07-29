from pydantic import BaseModel

class Spot(BaseModel):
    name: str
    latitude: float
    longitude: float
    spot_type: str
    description: str = None