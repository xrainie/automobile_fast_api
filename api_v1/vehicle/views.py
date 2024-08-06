from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.vehicle.schemas import VehicleQueryParamsSchema

from . import crud

from core.db_helper import get_db
from .schemas import VehicleSchema


router = APIRouter(tags=['vehicle'])


@router.get('/', response_model=VehicleSchema)
async def get_vehicles(session: Annotated[AsyncSession, Depends(get_db)], params: Annotated[VehicleQueryParamsSchema, Depends()]):
    await crud.get_vehicles(session=session, params=params)