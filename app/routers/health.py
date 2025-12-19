from fastapi import APIRouter

router = APIRouter(
    prefix = "/health",
    tags = ["Health"]
)

@router.get("/")
def health_check():
    return{
        "status" : "ok",
        "message" : "API backend is running"
    }