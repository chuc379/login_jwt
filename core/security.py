# app/core/security.py

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from login_jwt.core.database import SessionLocal
from login_jwt.core.jwt_encode import create_access_token
from login_jwt.core.jwt_decode import decode_access_token
from login_jwt.entities.user import User
from login_jwt.repositories.user_repository import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Password ---
def hash_password(password: str) -> str:
    return pwd_context.hash(password.encode("utf-8")[:72])

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password.encode("utf-8")[:72], hashed)

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    user_id = decode_access_token(credentials.credentials)
    repo = UserRepository(db)
    user = repo.find_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    return user
