from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import uuid

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "mysecret")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1 hour

auth_scheme = HTTPBearer()

# Create JWT
def create_jwt(user_id: int, email: str):
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "user_id": user_id,
        "email": email,
        "exp": expire.timestamp()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Verify JWT
def verify_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        exp = payload.get("exp")
        if exp is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token missing expiration")
        if datetime.now(timezone.utc).timestamp() > exp:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
        
        user_info = {
            "user_id": payload.get("sub"),
            "email": payload.get("email")
        }

        if user_info["user_id"] is None or user_info["email"] is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token missing user information")
        
        return user_info
    
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

# Dependency for protected routes
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = credentials.credentials
    return verify_jwt(token)

def create_refresh_token() -> str:
    return str(uuid.uuid4())