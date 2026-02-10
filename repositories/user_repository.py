from sqlalchemy.orm import Session
from login_jwt.entities.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def find_by_id(self, user_id: str):
        return self.db.query(User).filter(User.id == user_id).first()

    def create_user(self, username: str, email: str, password_hash: str):
        from uuid import uuid4
        user = User(
            id=uuid4(),
            username=username,
            email=email,
            password_hash=password_hash,
            is_active=True
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
