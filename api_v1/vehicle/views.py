from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.vehicle.schemas import VehicleQueryParamsSchema

from . import crud

from core.db_helper import get_db
from .schemas import VehicleSchema, CreateVehicleSchema, VehicleUpdatePartial

from .dependencies import vehicle_by_id


router = APIRouter(tags=['vehicle'], prefix='/api/cars')


@router.get('/', response_model=list[VehicleSchema])
async def get_vehicles(session: Annotated[AsyncSession, Depends(get_db)], params: Annotated[VehicleQueryParamsSchema, Depends()]) -> list[VehicleSchema]:
    return await crud.get_vehicles(session=session, params=params)


@router.post('/', response_model=VehicleSchema)
async def create_vehicle(session: Annotated[AsyncSession, Depends(get_db)], vehicle: CreateVehicleSchema):
   return await crud.create_vehicle(session=session, vehicle=vehicle)


@router.get('/{id}/', response_model=VehicleSchema)
async def get_vehicle(vehicle: VehicleSchema = Depends(vehicle_by_id)):
    return vehicle

@router.put('/{id}/', response_model=VehicleSchema)
async def update_vehicle(session: Annotated[AsyncSession, Depends(get_db)], vehicle_update: CreateVehicleSchema | VehicleUpdatePartial, vehicle: VehicleSchema = Depends(vehicle_by_id),):
    return await crud.update_vehicle(session, vehicle=vehicle, vehicle_update=vehicle_update)