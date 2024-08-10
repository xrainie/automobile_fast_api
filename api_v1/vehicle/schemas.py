from pydantic import BaseModel, Field
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
    brand: str = Field(min_length=2, examples=['марка машины'])
    model: str = Field(min_length=2, examples=['название модели машины'])
    year_of_issue:int = Field(gt=1949, lt=datetime.now().year)
    fuel: FuelTypes
    gearbox: GearBox
    mileage:int = Field(ge=0)


class CreateVehicleSchema(VehicleBase):
    price: int


class VehicleSchema(VehicleBase):
    price: int = Field(ge=0)
    id: int


class VehicleQueryParamsSchema(VehicleBase):
    brand: str | None = None
    model: str | None = None
    year_of_issue:int | None = Field(gt=1949, lt=datetime.now().year, title="Год выпуска автомобиля", default=None)
    fuel: FuelTypes | None = None
    gearbox: GearBox | None = None
    mileage: int | None = Field(ge=0, title="Пробег автомобиля", default=None)
    min_price: int | None = Field(ge=0, default=None)
    max_price: int | None = Field(default=None)


class VehicleUpdatePartial(CreateVehicleSchema):
    brand: str | None = None
    model: str | None = None
    year_of_issue:int | None = Field(gt=1949, lt=datetime.now().year, title="Год выпуска автомобиля", default=None)
    fuel: FuelTypes | None = None
    gearbox: GearBox | None = None
    mileage: int | None = Field(ge=0, title="Пробег автомобиля", default=None)
    min_price: int | None = Field(ge=0, default=None)
    max_price: int | None = Field(default=None)
