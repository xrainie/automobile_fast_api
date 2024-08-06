from .base import BaseModel
from sqlalchemy.orm import Mapped


class VehicleModel(BaseModel):
    brand: Mapped[str]
    model: Mapped[str]
    year_of_issue = Mapped[int]
    fuel = Mapped[str]
    gearbox = Mapped[str]
    mileage = Mapped[int]
    price = Mapped[int]