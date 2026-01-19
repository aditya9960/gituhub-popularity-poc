from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import router as v1_router # version 1

app = FastAPI(title=settings.APP_NAME)

app.include_router(v1_router, prefix=settings.API_V1_PREFIX)

@app.get("/health")
def health():
    return {"status": "ok"}