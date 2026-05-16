import pandas as pd

from datetime import datetime

from src.utils.csv_handler import (
    read_csv_data,
    write_csv_data
)


def register_user(payload):

    users_df = read_csv_data("users.csv")

    if not users_df.empty:

        existing_user = users_df[
            users_df["email"] == payload["email"]
        ]

        if not existing_user.empty:

            return {
                "status": False,
                "message": "Email already exists"
            }

    new_id = 1

    if not users_df.empty:
        new_id = users_df["id"].max() + 1

    new_user = {
        "id": new_id,
        "name": payload["name"],
        "email": payload["email"],
        "password": payload["password"],
        "role": "user",
        "is_approved": False,
        "created_at": datetime.now()
    }

    users_df = pd.concat(
        [
            users_df,
            pd.DataFrame([new_user])
        ],
        ignore_index=True
    )

    write_csv_data(
        "users.csv",
        users_df
    )

    return {
        "status": True,
        "message": "User registered successfully"
    }


def create_default_admin():

    users_df = read_csv_data("users.csv")

    if not users_df.empty:

        admin_exists = users_df[
            users_df["role"] == "admin"
        ]

        if not admin_exists.empty:
            return

    admin_user = {
        "id": 1,
        "name": "Admin",
        "email": "admin@gmail.com",
        "password": "admin123",
        "role": "admin",
        "is_approved": True,
        "created_at": datetime.now()
    }

    users_df = pd.concat(
        [
            users_df,
            pd.DataFrame([admin_user])
        ],
        ignore_index=True
    )

    write_csv_data(
        "users.csv",
        users_df
    )
