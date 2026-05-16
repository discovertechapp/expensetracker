import pandas as pd
from datetime import datetime

from src.utils.csv_handler import (
    read_csv_file,
    write_csv_file
)


def register_user(data):

    users_df = read_csv_file("users.csv")

    if not users_df.empty:
        if data["email"] in users_df["email"].values:
            return {
                "status": False,
                "message": "Email already exists"
            }

    new_id = 1

    if not users_df.empty:
        new_id = users_df["id"].max() + 1

    new_user = {
        "id": new_id,
        "name": data["name"],
        "email": data["email"],
        "password": data["password"],
        "role": "user",
        "is_approved": False,
        "created_at": datetime.now()
    }

    users_df = pd.concat(
        [users_df, pd.DataFrame([new_user])],
        ignore_index=True
    )

    write_csv_file("users.csv", users_df)

    return {
        "status": True,
        "message": "User registered successfully. Awaiting admin approval."
    }
