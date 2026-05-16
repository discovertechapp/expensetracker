from flask import Blueprint, request

from src.services.auth_service import register_user

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route("/login")
def login():

    return {
        "status": True,
        "message": "Login Route Working"
    }


@auth_bp.route("/register", methods=["POST"])
def register():

    payload = request.json

    response = register_user(payload)

    return response
