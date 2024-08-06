from fastapi import FastAPI

import uvicorn

from api_v1.vehicle.views import router as vehicle_router

from core.db_helper import db_helper

from core.models.base import BaseModel


async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(vehicle_router)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)