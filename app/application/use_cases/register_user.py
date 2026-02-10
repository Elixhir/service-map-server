from app.domain.repositories.user import UserRepository
from app.application.dtos.user import UserDTO
from app.domain.value_objects.email import Email
from app.domain.entities.user import User
from app.application.dependencies.hash_password import PasswordHasher

class RegisterUserUseCase:
    def __init__(self, user_repository: UserRepository, password_hasher: PasswordHasher):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    def execute(self, user_data: UserDTO):
        email = Email(user_data.email)
        hashed_password = self.password_hasher.hash(user_data.password)
        
        user = User.create(email = email, password_hash = hashed_password)
        
        if self.user_repository.exists_by_email(email):
            raise ValueError("User with this email already exists")
        
        self.user_repository.save(user)
        
        return user