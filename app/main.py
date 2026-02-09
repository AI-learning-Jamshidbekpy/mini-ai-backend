from fastapi import FastAPI
from app.core.config import get_settings
from app.api.routes.health import router as health_router

app = FastAPI(title=get_settings().API_V1)

app.include_router(health_router)





