from datetime import datetime

from src.utils.elasticsearch_handler import get_es_client
from src.utils.jwt_handler import generate_token

es = get_es_client()


# ---------------------------------------------------------
# Create Default Admin
# ---------------------------------------------------------
def create_default_admin():

    response = es.search(
        index="users",
        body={
            "query": {
                "term": {
                    "role.keyword": "admin"
                }
            }
        }
    )

    total = response["hits"]["total"]["value"]

    if total > 0:
        return

    admin_user = {
        "user_id": 1,
        "name": "Admin",
        "email": "admin@gmail.com",
        "password": "admin123",
        "role": "admin",
        "is_approved": True,
        "created_at": str(datetime.now())
    }

    es.index(
        index="users",
        document=admin_user
    )

    print("Default admin created")


# ---------------------------------------------------------
# Register User
# ---------------------------------------------------------
def register_user(payload):

    existing_user = es.search(
        index="users",
        body={
            "query": {
                "term": {
                    "email.keyword": payload["email"]
                }
            }
        }
    )

    total = existing_user["hits"]["total"]["value"]

    if total > 0:

        return {
            "status": False,
            "message": "Email already exists"
        }

    user_count = es.count(index="users")["count"]

    new_user = {
        "user_id": user_count + 1,
        "name": payload["name"],
        "email": payload["email"],
        "password": payload["password"],
        "role": "user",
        "is_approved": False,
        "created_at": str(datetime.now())
    }

    es.index(
        index="users",
        document=new_user
    )

    return {
        "status": True,
        "message": "User registered successfully"
    }


# ---------------------------------------------------------
# Login User
# ---------------------------------------------------------
def login_user(payload):

    response = es.search(
        index="users",
        body={
            "query": {
                "term": {
                    "email.keyword": payload["email"]
                }
            }
        }
    )

    total = response["hits"]["total"]["value"]

    if total == 0:

        return {
            "status": False,
            "message": "Invalid email"
        }

    user = response["hits"]["hits"][0]["_source"]

    if user["password"] != payload["password"]:

        return {
            "status": False,
            "message": "Invalid password"
        }

    if not user["is_approved"]:

        return {
            "status": False,
            "message": "User not approved by admin"
        }

    token = generate_token(user)

    return {
        "status": True,
        "message": "Login successful",
        "token": token,
        "data": {
            "user_id": user["user_id"],
            "name": user["name"],
            "email": user["email"],
            "role": user["role"]
        }
    }


# ---------------------------------------------------------
# Approve User
# ---------------------------------------------------------
def approve_user(user_id):

    response = es.search(
        index="users",
        body={
            "query": {
                "term": {
                    "user_id": user_id
                }
            }
        }
    )

    total = response["hits"]["total"]["value"]

    if total == 0:

        return {
            "status": False,
            "message": "User not found"
        }

    hit = response["hits"]["hits"][0]

    doc_id = hit["_id"]

    user = hit["_source"]

    user["is_approved"] = True

    es.index(
        index="users",
        id=doc_id,
        document=user
    )

    return {
        "status": True,
        "message": "User approved successfully"
    }
