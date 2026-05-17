from datetime import datetime

from src.utils.elasticsearch_handler import get_es_client
from src.utils.jwt_handler import generate_token

es = get_es_client()


# ---------------------------------------------------------
# Create Default Admin
# ---------------------------------------------------------
def create_default_admin():

    try:

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

    except Exception as e:
        print("Admin creation error:", str(e))


# ---------------------------------------------------------
# Register User
# ---------------------------------------------------------
def register_user(payload):

    try:

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

        if existing_user["hits"]["total"]["value"] > 0:

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

    except Exception as e:

        return {
            "status": False,
            "message": str(e)
        }


# ---------------------------------------------------------
# Login User
# ---------------------------------------------------------
def login_user(payload):

    try:

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

    except Exception as e:

        return {
            "status": False,
            "message": str(e)
        }


# ---------------------------------------------------------
# Get All Users (Admin)
# ---------------------------------------------------------
def get_all_users_service():

    try:

        response = es.search(
            index="users",
            body={
                "query": {
                    "match_all": {}
                },
                "size": 1000
            }
        )

        users = []

        for hit in response["hits"]["hits"]:

            user = hit["_source"]
            user["document_id"] = hit["_id"]

            users.append(user)

        return {
            "status": True,
            "data": users
        }

    except Exception as e:

        return {
            "status": False,
            "message": str(e)
        }


# ---------------------------------------------------------
# Approve User (Admin)
# ---------------------------------------------------------
def approve_user_service(document_id):

    try:

        es.update(
            index="users",
            id=document_id,
            body={
                "doc": {
                    "is_approved": True
                }
            }
        )

        return {
            "status": True,
            "message": "User approved successfully"
        }

    except Exception as e:

        return {
            "status": False,
            "message": str(e)
        }


# ---------------------------------------------------------
# Delete User (Admin)
# ---------------------------------------------------------
def delete_user_service(document_id):

    try:

        es.delete(
            index="users",
            id=document_id
        )

        return {
            "status": True,
            "message": "User deleted successfully"
        }

    except Exception as e:

        return {
            "status": False,
            "message": str(e)
        }
