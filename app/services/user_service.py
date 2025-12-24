from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password, create_access_token

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed = hash_password(user.password)
    db_user = User(email = user.email, hashed_password = hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(db, email: str, password: str):
    user = get_user_by_email(db, email)

    if not user:
        return None
    
    if not verify_password(password, user.hashed_password):
        return None
    
    token_data = {
        "sub" : str(user.id),
        "email" : user.email
    }
    access_token = create_access_token(token_data)
    return access_token