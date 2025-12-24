from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserLogin, TokenResponse
from app.services.user_service import get_user_by_email, create_user, login_user
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

@router.post("/login", response_model = TokenResponse)
def login(data: UserLogin, db: Session = Depends(get_db)):
    token = login_user(db, data.email, data.password)

    if not token:
        raise HTTPException(
            status_codes = status.HTTP_401_UNAUTHORIZED,
            detail = "invalid credentials"
        )
    return { "access_token": token}