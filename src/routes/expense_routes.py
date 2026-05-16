from flask import Blueprint, request

from src.services.expense_service import (
    create_expense,
    get_expenses
)

expense_bp = Blueprint("expense_bp", __name__)


# ---------------------------------------------------------
# Create Expense
# ---------------------------------------------------------
@expense_bp.route("/expenses", methods=["POST"])
def add_expense():

    payload = request.json

    response = create_expense(payload)

    return response


# ---------------------------------------------------------
# Get Expenses
# ---------------------------------------------------------
@expense_bp.route("/expenses", methods=["GET"])
def expenses():

    user_id = request.args.get("user_id")

    response = get_expenses(user_id)

    return response
