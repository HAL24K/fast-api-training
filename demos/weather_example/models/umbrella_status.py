from pydantic import BaseModel


class UmbrellaStatus(BaseModel):
    bring_umbrella: bool
    temp: float
    weather: str
