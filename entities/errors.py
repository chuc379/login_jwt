class DomainError(Exception):
    code: str = "DOMAIN_ERROR"

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class PermissionDenied(DomainError):
    code = "PERMISSION_DENIED"


class UsernameAlreadyExists(DomainError):
    code = "USERNAME_EXISTS"
