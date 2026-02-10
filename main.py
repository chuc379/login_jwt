from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import status, HTTPException

from controllers.all_controller import router as auth_router
from schemas.exceptions import domain_exception_handler
from entities.errors import DomainError

app = FastAPI(title="Auth Service")

# ---- Security scheme ----
bearer_scheme = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    if token != "test-token":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return {"user_id": "demo"}

# ---- Include router ----
app.include_router(auth_router)

# ---- Register global exception handler ----
app.add_exception_handler(DomainError, domain_exception_handler)
