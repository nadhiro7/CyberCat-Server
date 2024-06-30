from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from models.models import User
from users.schemas import UserSchema


user_bp = Blueprint("users", __name__)


@user_bp.get("/all")
@jwt_required()
def get_all_users():
    # claims = get_jwt()

    # if claims.get("is_staff") == True:
    page = request.args.get("page", default=1, type=int)

    per_page = request.args.get("per_page", default=3, type=int)

    users = User.query.paginate(page=page, per_page=per_page)

    result = UserSchema().dump(users, many=True)

    return (
        jsonify(
        {
                "users": result,
            }
        ),
        200,
    )

    # return jsonify({"message": "You are not authorized to access this"}), 401

@user_bp.post("/addUser")
def register_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    telegram_username = data.get("telegram_username")
    if username is None or email is None or password is None or telegram_username is None:
        return jsonify({"error": "Missing data"}), 400
    else:
        user = User.get_user_by_username(username=data.get("username"))

        if user is not None:
            return jsonify({"error": "User already exists"}), 409

        new_user = User(username=username, email=email,telegram_username=telegram_username)

        new_user.set_password(password=data.get("password"))

        new_user.save()

        return jsonify({"message": "User created"}), 201
