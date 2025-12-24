from fastapi import APIRouter, Depends
from app.utils.jwt_utils import get_current_user

router = APIRouter(prefix = "/profile", tags = ["Profile"])

@router.get("/see_profile")
def see_profile(current_user: dict = Depends(get_current_user)):
    return {"message" : "User profile", "user": current_user}

@router.post("/update-password")
def update_password(new_password: str, current_user: dict = Depends(get_current_user)):
    return {"message" : "Password updated successfully", "user" : current_user}