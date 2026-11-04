from fastapi import FastAPI

from app.api.routes import health
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="A multi-user task management API.",)

app.include_router(health.router)

@app.get("/")
def read_root():
    return {"name": settings.app_name, "docs": "/docs"}
