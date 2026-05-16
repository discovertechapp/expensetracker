import jwt

from datetime import datetime, timedelta

SECRET_KEY = "expense_tracker_secret"


# ---------------------------------------------------------
# Generate JWT Token
# ---------------------------------------------------------
def generate_token(user):

    payload = {
        "user_id": user["user_id"],
        "email": user["email"],
        "role": user["role"],
        "exp": datetime.utcnow() + timedelta(days=1)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

    return token


# ---------------------------------------------------------
# Verify JWT Token
# ---------------------------------------------------------
def verify_token(token):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        return payload

    except Exception:

        return None
