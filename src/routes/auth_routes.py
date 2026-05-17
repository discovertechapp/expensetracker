from flask import Blueprint, request, jsonify

from src.services.auth_service import (
    register_user,
    login_user,
    get_all_users_service,
    approve_user_service,
    delete_user_service
)

auth_bp = Blueprint("auth_bp", __name__)


# ---------------------------------------------------------
# Register
# ---------------------------------------------------------
@auth_bp.route("/register", methods=["POST"])
def register():

    payload = request.json

    response = register_user(payload)

    return jsonify(response)


# ---------------------------------------------------------
# Login
# ---------------------------------------------------------
@auth_bp.route("/login", methods=["POST"])
def login():

    payload = request.json

    response = login_user(payload)

    return jsonify(response)


# ---------------------------------------------------------
# Get all users (ADMIN)
# ---------------------------------------------------------
@auth_bp.route("/users", methods=["GET"])
def get_users():

    response = get_all_users_service()

    return jsonify(response)


# ---------------------------------------------------------
# Approve user (ADMIN)
# ---------------------------------------------------------
@auth_bp.route("/users/<document_id>/approve", methods=["PUT"])
def approve_user(document_id):

    response = approve_user_service(document_id)

    return jsonify(response)


# ---------------------------------------------------------
# Delete user (ADMIN)
# ---------------------------------------------------------
@auth_bp.route("/users/<document_id>", methods=["DELETE"])
def delete_user(document_id):

    response = delete_user_service(document_id)

    return jsonify(response)
