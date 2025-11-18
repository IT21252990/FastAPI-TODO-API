from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.user import User
from app.core.security import hash_password, verify_password

# Create New User
def create_user(db:Session, username:str, email:str, password:str) -> User:
    user = User(
        username = username,
        email = email,
        hashed_password = hash_password(password)
    )
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        return None
    return user

# Get User by Email
def get_user_by_email(db:Session, email:str):
    return db.query(User).filter(User.email == email).first()

# Get User by Username
def get_user_by_username(db:Session, username:str):
    return db.query(User).filter(User.username == username).first()

# Authenticate User
def authenticate_user(db:Session, username:str, password:str):
    user = get_user_by_username(db, username)

    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user