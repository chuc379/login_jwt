from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.auth_schema import LoginRequest, TokenResponse
from core.security import get_current_user,get_db

from repositories.user_repository import UserRepository
from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])



@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    service = AuthService(repo)

    token = service.login(data.username, data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"access_token": token}

