import pandas as pd

from datetime import datetime

from src.utils.csv_handler import (
    read_csv_data,
    write_csv_data
)


def add_expense(payload):

    expenses_df = read_csv_data("expenses.csv")

    new_id = 1

    if not expenses_df.empty:
        new_id = expenses_df["id"].max() + 1

    expense = {
        "id": new_id,
        "user_id": payload["user_id"],
        "main_category": payload["main_category"],
        "sub_category": payload["sub_category"],
        "amount": payload["amount"],
        "description": payload.get("description", ""),
        "expense_date": payload["expense_date"],
        "created_at": datetime.now()
    }

    expenses_df = pd.concat(
        [
            expenses_df,
            pd.DataFrame([expense])
        ],
        ignore_index=True
    )

    write_csv_data(
        "expenses.csv",
        expenses_df
    )

    return {
        "status": True,
        "message": "Expense added successfully"
    }
