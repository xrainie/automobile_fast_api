from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, Path, Depends, status
from typing import Annotated

from api_v1.vehicle.schemas import VehicleSchema
from core.db_helper import get_db

from . import crud

async def vehicle_by_id(session: Annotated[AsyncSession, Depends(get_db)], id: Annotated[int, Path]) -> VehicleSchema:
    vehicle = await crud.get_vehicle(session=session, id=id)
    
    if vehicle is not None:
        return vehicle
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND
    )