from flask import Blueprint, request, jsonify
from app.application.dtos.user import UserDTO
from app.presentation.v1.injections.auth import get_register_user_use_case, get_login_user_use_case
from app.presentation.v1.injections.auth import jwt_service

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

register_user_use_case = get_register_user_use_case()
login_user_use_case = get_login_user_use_case()
get_jwt_service = jwt_service()

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    try:
        entry_data = UserDTO(
            email=data["email"],
            password=data["password"]
        )

        user = register_user_use_case.execute(entry_data)

        return jsonify({
            "id": user.id,
            "email": user.email.value
        }), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    try:
        entry_data = UserDTO(
            email=data["email"],
            password=data["password"]
        )

        user = login_user_use_case.execute(entry_data)
        token = get_jwt_service.generate_access_token(user.id)
        
        return jsonify({
            "id": user.id,
            "email": user.email.value,
            "access_token": token
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400