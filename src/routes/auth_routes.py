from flask import Blueprint, request

from src.services.auth_service import (
    register_user,
    login_user,
    approve_user
)

auth_bp = Blueprint("auth_bp", __name__)


# ---------------------------------------------------------
# Register
# ---------------------------------------------------------
@auth_bp.route("/register", methods=["POST"])
def register():

    payload = request.json

    response = register_user(payload)

    return response


# ---------------------------------------------------------
# Login
# ---------------------------------------------------------
@auth_bp.route("/login", methods=["POST"])
def login():

    payload = request.json

    response = login_user(payload)

    return response


# ---------------------------------------------------------
# Approve User
# ---------------------------------------------------------
@auth_bp.route("/approve-user/<int:user_id>", methods=["PUT"])
def approve(user_id):

    response = approve_user(user_id)

    return response
