from fastapi import FastAPI
from app.routers import health
from app.routers import auth

app = FastAPI(
    title = "API-auth",
    description = "Authentication and Authorization Service",
    version = "1.0.0"
)

app.include_router(health.router)
app.include_router(auth.router)