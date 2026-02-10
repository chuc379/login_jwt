from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from entities.errors import DomainError
from schemas.CreateUser_schema import ErrorCreateUserResponse

# --- Global handler ---
def domain_exception_handler(request: Request, exc: DomainError):
    return JSONResponse(
        status_code=400,
        content=ErrorCreateUserResponse(
            code=getattr(exc, "code", "DOMAIN_ERROR"),
            message=str(exc)
        ).dict()
    )
