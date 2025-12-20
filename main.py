from fastapi import FastAPI
from app.routers import health

app = FastAPI(
    title = "API-auth",
    description = "Authentication and Authorization Service",
    version = "1.0.0"
)

app.include_router(health.router)