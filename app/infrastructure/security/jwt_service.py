import jwt
from datetime import datetime, timedelta
from flask import current_app

class JWTService:
    def generate_access_token(self, user_id: int) -> str:
        payload = {
            "sub": str(user_id),
            "exp": datetime.utcnow() + timedelta(hours=2)
        }

        return jwt.encode(
            payload,
            current_app.config["JWT_SECRET_KEY"],
            algorithm="HS256"
        )
