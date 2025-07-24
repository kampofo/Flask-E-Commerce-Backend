from flask import Blueprint, jsonify, abort
from app.mock_data import users

users_bp = Blueprint("users", __name__, url_prefix="/api/v1/users")


@users_bp.route("", methods=["GET"])
def get_users():
    return jsonify(users)


@users_bp.route("/<int:id>", methods=["GET"])
def get_user(id):
    user = next((u for u in users if u["id"] == id), None)
    if not user:
        abort(404, description="User not found")
    return jsonify(user)
