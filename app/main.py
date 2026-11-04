from fastapi import FastAPI

from app.api.routes import health

app = FastAPI(title="TaskFlow API",
    version="0.1.0",
    description="A multi-user task management API.",)

app.include_router(health.router)

@app.get("/")
def read_root():
    return {"name": "TaskFlow API", "docs": "/docs"}
