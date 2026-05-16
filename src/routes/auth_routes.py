from flask import Blueprint, request

from src.services.auth_service import register_user
from src.services.auth_service import login_user

auth_bp = Blueprint("auth_bp", __name__)



@auth_bp.route("/login", methods=["POST"])
def login():

    payload = request.json

    response = login_user(payload)

    return response


@auth_bp.route("/register", methods=["POST"])
def register():

    payload = request.json

    response = register_user(payload)

    return response



