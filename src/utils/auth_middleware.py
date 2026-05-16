from functools import wraps

from flask import request

from src.utils.jwt_handler import verify_token


# ---------------------------------------------------------
# JWT Authentication Decorator
# ---------------------------------------------------------
def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if "Authorization" in request.headers:

            auth_header = request.headers[
                "Authorization"
            ]

            token = auth_header.replace(
                "Bearer ",
                ""
            )

        if not token:

            return {
                "status": False,
                "message": "Token missing"
            }, 401

        payload = verify_token(token)

        if not payload:

            return {
                "status": False,
                "message": "Invalid or expired token"
            }, 401

        request.user = payload

        return f(*args, **kwargs)

    return decorated
