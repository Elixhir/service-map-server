from uuid import UUID, uuid4
from app.domain.value_objects.email import Email
from werkzeug.security import generate_password_hash

class User:
    def __init__(
        self,
        email: Email,
        password_hash: str,
        is_active: bool = True,
        user_id: UUID | None = None
    ):
        if not password_hash:
            raise ValueError("Password hash is required")

        self.id = user_id or uuid4()
        self.email = email
        self.password_hash = password_hash
        self.is_active = is_active

    def deactivate(self):
        self.is_active = False

    @classmethod
    def create(cls, email: Email, password_hash: str):
        return cls(
            email=email,
            password_hash=password_hash
        )