from src.utils.csv_handler import read_csv_file


def get_dashboard_summary(user_id):

    expenses_df = read_csv_file("expenses.csv")

    if expenses_df.empty:
        return {}

    user_expenses = expenses_df[
        expenses_df["user_id"] == user_id
    ]

    total_expense = user_expenses["amount"].sum()

    category_summary = (
        user_expenses
        .groupby("main_category_id")["amount"]
        .sum()
        .to_dict()
    )

    return {
        "total_expense": total_expense,
        "category_summary": category_summary
    }
