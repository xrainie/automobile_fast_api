from ast import stmt
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from .schemas import VehicleQueryParamsSchema, VehicleSchema, CreateVehicleSchema, VehicleUpdatePartial
from core.models import VehicleModel
from fastapi import Depends, HTTPException, Query, status
from typing import Annotated


async def get_vehicles(session: AsyncSession, params: Annotated[VehicleQueryParamsSchema, Depends()]):
    paramsdict = params.model_dump(exclude_none=True, exclude_unset=True)
    # offset_min = page * size
    # offset_max = (page + 1) * size
    print(paramsdict)
    stmt = select(VehicleModel)
    if 'brand' in paramsdict:
        stmt = stmt.where(VehicleModel.brand == paramsdict['brand'])
    if 'model' in paramsdict:
        stmt = stmt.where(VehicleModel.model == paramsdict['model'])
    if 'year_of_issue' in paramsdict:
        stmt = stmt.where(VehicleModel.year_of_issue == paramsdict['year_of_issue'])
    if 'fuel' in paramsdict:
        stmt = stmt.where(VehicleModel.fuel == paramsdict['fuel'])
    if 'gearbox' in paramsdict:
        stmt = stmt.where(VehicleModel.gearbox == paramsdict['gearbox'])
    if 'mileage' in paramsdict:
        stmt = stmt.where(VehicleModel.mileage == paramsdict['mileage'])
    if 'min_price' in paramsdict:
        stmt = stmt.where(VehicleModel.price >= paramsdict['min_price'])
    if 'max_price' in paramsdict:
        stmt = stmt.where(VehicleModel.price <= paramsdict['max_price'])
                
    result: Result = await session.execute(stmt)
    vehicles = result.scalars().all()
    return list(vehicles)


async def create_vehicle(session: AsyncSession, vehicle: CreateVehicleSchema) -> VehicleSchema:
    vehicle_inst = VehicleModel(**vehicle.model_dump())
    session.add(vehicle_inst)
    await session.commit()
    return vehicle_inst


async def get_vehicle(session: AsyncSession, id: int) -> VehicleSchema:
    return await session.get(VehicleModel, id)


async def update_vehicle(session: AsyncSession, vehicle: VehicleSchema, vehicle_update: CreateVehicleSchema | VehicleUpdatePartial, partial: bool = True) -> VehicleSchema:
    for name, value in vehicle_update.model_dump(exclude_unset=partial).items():
        setattr(vehicle, name, value)
    await session.commit()
    return vehicle