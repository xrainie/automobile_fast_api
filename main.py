from fastapi import FastAPI

import uvicorn

from api_v1.vehicle.views import router as vehicle_router

app = FastAPI()
app.include_router(vehicle_router)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)