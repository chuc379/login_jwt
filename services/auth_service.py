from repositories.user_repository import UserRepository
from core.security import verify_password, create_access_token

class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def login(self, username: str, password: str):
        user = self.repo.find_by_username(username)
        if not user:
            return None

        if not verify_password(password, user.password_hash):
            return None

        token = create_access_token({"sub": str(user.id)})
        return token
