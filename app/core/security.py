from passlib.context import CryptContext
from fastapi import FastAPI, Depends, HTTPException, Header, status
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import jwt, JWTError
from dotenv import load_dotenv
import os 

load_dotenv()

IMPORTED_SECRET_KEY = os.getenv("SECRET_KEY")
IMPORTED_ALGORITHM = os.getenv("ALGORITHM")
IMPORTED_ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

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
    expire = datetime.utcnow() + timedelta(minutes =int(IMPORTED_ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update( {"exp" : expire})
    token = jwt.encode(to_encode, IMPORTED_SECRET_KEY, algorithm=IMPORTED_ALGORITHM)
    return token

def decode_toke(token: str):
    try:
        payload = jwt.decode(token, IMPORTED_SECRET_KEY, algorithms=[IMPORTED_ALGORITHM])
        return payload
    except JWTError:
        return None