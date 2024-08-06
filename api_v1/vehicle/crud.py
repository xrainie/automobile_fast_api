from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .schemas import VehicleQueryParamsSchema, VehicleSchema
from core.models import VehicleModel
from fastapi import Depends, HTTPException, status
from typing import Annotated


attrs = ["brand", "model", "year_of_issue", "fuel", "gearbox", "mileage", "min_price", "max_price"]


async def get_vehicles(session: AsyncSession, params: Annotated[VehicleQueryParamsSchema, Depends()]):
    paramsdict = params.model_dump(exclude_unset=True)
    stmt = select(VehicleModel)
    if 'brand' in paramsdict:
        stmt = stmt.where(VehicleModel.brand == paramsdict['brand'])
    if 'model' in paramsdict:
        stmt = stmt.where(VehicleModel.model == paramsdict['brand'])
    if 'year_of_issue' in paramsdict:
        stmt = stmt.where(VehicleModel.year_of_issue == paramsdict['brand'])
    if 'fuel' in paramsdict:
        stmt = stmt.where(VehicleModel.fuel == paramsdict['brand'])
    if 'gearbox' in paramsdict:
        stmt = stmt.where(VehicleModel.gearbox == paramsdict['brand'])
    if 'mileage' in paramsdict:
        stmt = stmt.where(VehicleModel.mileage == paramsdict['brand'])
    if 'min_price' in paramsdict:
        stmt = stmt.where(VehicleModel.price >= paramsdict['min_price'])
    if 'max_price' in paramsdict:
        stmt = stmt.where(VehicleModel.price <= paramsdict['max_price'])
                
    result = await session.execute(stmt)

    if result is not None:
        return result
    
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='По заданным фильтрам ничего не найдено.')