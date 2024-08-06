from operator import gt
from pydantic import BaseModel, PastDatetime, Field
from enum import Enum
from datetime import datetime
from typing import Annotated, Optional


class FuelTypes(str, Enum):
    Petrol = "Бензин"
    Diesel = "Дизель"
    Hybrid = "Гибрид"
    Electricity = "Электричество"


class GearBox(str, Enum):
    Mechanical = "Механика"
    Auto = "Автоматическая"
    Variator = "Вариатор"
    Robot = "Робот"


class VehicleBase(BaseModel):
    brand: str
    model: str
    year_of_issue:int = Field(gt=1800, lt=datetime.now().year, title="Год выпуска автомобиля")
    fuel: Annotated[str, FuelTypes]
    gearbox: Annotated[str, GearBox]
    mileage:int = Field(gt=1, title="Пробег автомобиля")


class CreateVehicleSchema(VehicleBase):
    pass


class VehicleSchema(VehicleBase):
    id: int
    price: int


class VehicleQueryParamsSchema(VehicleBase):
    brand: str = None
    model: str = None
    year_of_issue:int = Field(gt=1949, lt=datetime.now().year, title="Год выпуска автомобиля", default=None)
    fuel: FuelTypes = None
    gearbox: GearBox = None
    mileage: int = Field(ge=0, title="Пробег автомобиля", default=None)
    min_price: int = Field(gt=0, default=None)
    max_price: int = Field(default=None)
