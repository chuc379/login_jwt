from sqlalchemy import Column, String, Boolean, TIMESTAMP, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from login_jwt.core.database import Base
import uuid

class Role(Base):
    __tablename__ = "roles"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    # relationship ngược (nếu muốn)
    users = relationship("User", back_populates="role")


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    # Mỗi user có 1 role
    role_id = Column(Integer, ForeignKey("auth.roles.id"))
    role = relationship("Role", back_populates="users")
