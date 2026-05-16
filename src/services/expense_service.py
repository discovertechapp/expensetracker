import pandas as pd
from datetime import datetime

from src.utils.csv_handler import (
    read_csv_file,
    write_csv_file
)


def add_expense(data):

    expenses_df = read_csv_file("expenses.csv")

    new_id = 1

    if not expenses_df.empty:
        new_id = expenses_df["id"].max() + 1

    expense = {
        "id": new_id,
        "user_id": data["user_id"],
        "main_category_id": data["main_category_id"],
        "sub_category_id": data["sub_category_id"],
        "amount": data["amount"],
        "description": data.get("description", ""),
        "expense_date": data["expense_date"],
        "created_at": datetime.now()
    }

    expenses_df = pd.concat(
        [expenses_df, pd.DataFrame([expense])],
        ignore_index=True
    )

    write_csv_file("expenses.csv", expenses_df)

    return {
        "status": True,
        "message": "Expense added successfully"
    }
