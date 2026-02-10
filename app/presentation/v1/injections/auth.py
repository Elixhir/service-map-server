from app.infrastructure.repositories.user import UserRepositoryImplementation
from app.domain.repositories.user import UserRepository
from app.application.use_cases.register_user import RegisterUserUseCase
from app.application.dependencies.hash_password import PasswordHasher

def get_user_repository() -> UserRepository:
    return UserRepositoryImplementation()

def get_register_user_use_case() -> RegisterUserUseCase:
    user_repository = get_user_repository()
    return RegisterUserUseCase(user_repository, password_hasher=PasswordHasher())
