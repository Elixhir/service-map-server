from app.application.dependencies.hash_password import PasswordHasher
from app.domain.repositories.user import UserRepository
from app.domain.entities.user import User
from app.application.dtos.user import UserDTO
from app.domain.value_objects.email import Email

class LoginUserUseCase:
    def __init__(self, user_repository: UserRepository, password_hasher: PasswordHasher):
        self.user_repository = user_repository
        self.password_hasher = password_hasher
    
    def execute(self, user_data: UserDTO) -> User:
        email = Email(user_data.email)
        user: User = self.user_repository.find_by_email(email)
        if not user:
            raise ValueError("Invalid credentials")
        if not self.password_hasher.verify(user_data.password, user.password_hash):
            raise ValueError("Invalid credentials")
        return user