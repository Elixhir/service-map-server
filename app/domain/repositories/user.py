from abc import ABC, abstractmethod
from app.domain.entities.user import User

class UserRepository(ABC):
    
    @abstractmethod
    def save(self, user_data: User) -> None:
        pass

    @abstractmethod
    def exists_by_email(self, email: str) -> bool:
        pass
    
    @abstractmethod
    def find_by_email(self, email: str) -> bool:
        pass
    