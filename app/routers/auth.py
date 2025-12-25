from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserLogin, TokenResponse, RefreshTokenRequest
from app.services.user_service import get_user_by_email, create_user, login_user
from app.database.session import get_db
from app.utils.jwt_utils import create_jwt, create_refresh_token
from datetime import datetime, timedelta, timezone
from app.models.refresh_token import RefreshToken

router = APIRouter(prefix = "/auth", tags = ["Auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user :
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Email already registered"
        )
    new_user = create_user(db, user)
    return new_user

@router.post("/login", response_model = TokenResponse)
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = login_user(db, data.email, data.password)

    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "invalid credentials"
        )
    
    access_token = create_jwt(user_id=user.id, email=user.email)
    refresh_token = create_refresh_token()
    expires_at = datetime.now(timezone.utc) + timedelta(days=7)


    db_refresh = RefreshToken(
        token = refresh_token,
        user_id = user.id,
        expires_at = expires_at
    )

    db.add(db_refresh)
    db.commit()

    return { 
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/refresh")
def refresh_access_token(data: RefreshTokenRequest, db: Session = Depends(get_db)):
    token_entry = db.query(RefreshToken).filter(
        RefreshToken.token == data.refresh_token
    ).first()

    if not token_entry:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    if token_entry.expires_at < datetime.now(timezone.utc):
        db.delete(token_entry)
        db.commit()
        raise HTTPException(status_code=401, detail="Refres token expired")
    
    new_access_token = create_jwt({"sub": str(token_entry.user_id)})
    return {"access_token": new_access_token}

@router.post("/logout")
def logout(data: RefreshTokenRequest, db: Session = Depends(get_db)):
    token_entry = db.query(RefreshToken).filter(
        RefreshToken.token == data.refresh_token

    ).first()

    if token_entry:
        db.delete(token_entry)
        db.commit()

    return {"message" : "logged out successsylly"}