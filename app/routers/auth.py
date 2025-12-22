from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import get_user_by_email, create_user
from app.database.session import get_db

router = APIRouter(prefix = "/auth", tags = ["Auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user :
        raise HTTPException(
            status_codes = status.HTTP_400_BAD_REQUEST,
            detail = "Email already registered"
        )
    new_user = create_user(db, user)
    return new_user