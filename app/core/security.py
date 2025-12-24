from passlib.context import CryptContext
from fastapi import FastAPI, Depends, HTTPException, Header, status
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import jwt, JWTError
from dotenv import load_dotenv
import os 

load_dotenv()

IMPORTED_SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(
    schemes = ["argon2"],
    deprecated = "auto"
)
 
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password) 

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update( {"exp" : expire})
    token = jwt.encode(to_encode, IMPORTED_SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_toke(token: str):
    try:
        payload = jwt.decode(token, IMPORTED_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None