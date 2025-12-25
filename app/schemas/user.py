from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    email: EmailStr
    password : str

class UserResponse(BaseModel):
    id : int
    email : EmailStr

    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email : str
    password : str

class TokenResponse(BaseModel):
    access_token : str
    refresh_token : str
    token_type : str = "bearer"

class RefreshTokenRequest(BaseModel):
    refresh_token: str