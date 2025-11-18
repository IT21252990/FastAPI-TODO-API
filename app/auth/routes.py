from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

from app.database import get_db
from app.schemas.user import UserCreate, UserOut, Token
from app.auth import crud_user
from app.core.security import create_access_token
from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])

# Register a new user
@router.post("/register", response_model=UserOut)
def register(user_in:UserCreate, db:Session = Depends(get_db)):
    existing_user = crud_user.get_user_by_username(db, user_in.username)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered!")
    
    user = crud_user.create_user(db, user_in.username, user_in.email, user_in.password)

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error Creating User!")
    
    return user

# Login user and return JWT
@router.post("/login",response_model=Token)
def login(form_data:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = crud_user.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Username or Password!")
    
    access_token = create_access_token({"sub":user.username})

    return {"access_token": access_token, "token_type": "bearer"}

# OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# Get current authenticated user
def get_current_user(token:str = Depends(oauth2_scheme),db:Session = Depends(get_db)) -> UserOut :
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials!", headers={"WWW-Authenticate": "Bearer"})

    try:
        # Decode JWT token
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username:str = payload.get("sub")
        if username is None:
            raise credential_exception
        
    except JWTError:
        raise credential_exception
        
    # Get user from Database
    user = crud_user.get_user_by_username(db, username)
    if user is None:
        raise credential_exception
    
    return user

# Get current user INFO
@router.get("/me", response_model=UserOut)
def read_users_me(current_user:UserOut = Depends(get_current_user)):
    return current_user