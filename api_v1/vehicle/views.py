from fastapi import APIRouter, Depends
from typing import Annotated, List
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.vehicle.schemas import VehicleQueryParamsSchema

from . import crud

from core.db_helper import get_db
from .schemas import VehicleSchema, CreateVehicleSchema


router = APIRouter(tags=['vehicle'], prefix='/api/cars')


@router.get('/', response_model=list[VehicleSchema])
async def get_vehicles(session: Annotated[AsyncSession, Depends(get_db)], params: Annotated[VehicleQueryParamsSchema, Depends()]) -> list[VehicleSchema]:
    return await crud.get_vehicles(session=session, params=params)


@router.post('/', response_model=VehicleSchema)
async def create_vehicle(session: Annotated[AsyncSession, Depends(get_db)], vehicle: CreateVehicleSchema):
   return await crud.create_vehicle(session=session, vehicle=vehicle)