from pydantic import BaseModel, EmailStr

# Shared User Properties
class UserBase(BaseModel):
    username:str
    email:EmailStr

# For User Registration
class UserCreate(UserBase):
    password:str

# For User Login
class UserLogin(UserBase):
    username:str
    password:str

# Returned to the Client
class UserOut(UserBase):
    id:int

    class Config:
        orm_mode = True

# Token Response
class Token(BaseModel):
    access_token:str
    token_type: str = "bearer"