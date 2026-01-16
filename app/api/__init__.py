# api router setup
from fastapi import APIRouter
# dummy version
from app.api.v1 import router as v1_router

# Create a main API router
api_router = APIRouter()

# use version
api_router.include_router(v1_router, prefix="/api/v1", tags=["v1"])