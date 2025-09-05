from fastapi import FastAPI
from .routers import health

app = FastAPI(title="PulseWatch")

app.include_router(health.router, prefix="/health", tags=["health"])

@app.get("/")
def root():
    return {"service": "pulsewatch", "status": "ok"}
