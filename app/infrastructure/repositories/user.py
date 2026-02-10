from app.domain.repositories.user import UserRepository
from app.domain.entities.user import User
from app.infrastructure.db.extensions  import db
from app.infrastructure.models.user import UserModel
from app.domain.value_objects.email import Email

class UserRepositoryImplementation(UserRepository):

    def save(self, user: User) -> None:
        model = UserModel(
            email=user.email.value,
            password_hash=user.password_hash,
        )
        db.session.add(model)
        db.session.commit()
    
    def exists_by_email(self, email: Email) -> bool:
        return (
            db.session.query(UserModel)
            .filter_by(email=email.value)
            .first()
            is not None
        )
    
    def find_by_email(self, email: Email) -> User:
        user_model = (
            db.session.query(UserModel)
            .filter_by(email=email.value)
            .first()
        )
        if user_model is None:
            return None
        return User(
            id=user_model.id,
            email=Email(user_model.email),
            password_hash=user_model.password_hash
        )