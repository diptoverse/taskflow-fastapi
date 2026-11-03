from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"name": "TaskFlow API", "docs": "/docs"}
