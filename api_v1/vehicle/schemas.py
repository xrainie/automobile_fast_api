from pydantic import BaseModel, PastDatetime, Field
from enum import Enum
from datetime import datetime
from typing import Annotated

class FuelTypes(Enum):
    Petrol = "Бензин"
    Diesel = "Дизель"
    Hybrid = "Гибрид"
    Electricity = "Электричество"


class GearBox(Enum):
    Mechanical = "Механика"
    Auto = "Автоматическая"
    Variator = "Вариатор"
    Robot = "Робот"


class VehicleBase(BaseModel):
    brand: str
    model: str
    year_of_issue = Field(PastDatetime.year, gt=1800, lt=datetime.now().year)
    fuel: Annotated[str, FuelTypes]
    gearbox: Annotated[str, GearBox]
    mileage: int
    price: int

class CreateVehicleSchema(VehicleBase):
    pass


class VehicleSchema(VehicleBase):
    id: int