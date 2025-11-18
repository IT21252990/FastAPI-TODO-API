from datetime import datetime, timedelta
from typing import Optional

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Password Hashing Helpers
def hash_password(password:str) -> str :
    # bcrypt supports max 72 bytes
    password = password[:72]
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str) -> bool :
    plain_password = plain_password[:72]
    return pwd_context.verify(plain_password,hashed_password)

# JWT Token Helpers
def create_access_token(data:dict, expires_delta:Optional[timedelta]=None):
    to_encode = data.copy()

    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))

    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return encoded_jwt