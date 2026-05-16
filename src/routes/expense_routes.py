from flask import Blueprint, request

from src.services.expense_service import (
    create_expense,
    get_expenses,
    update_expense,
    delete_expense
)
from src.utils.auth_middleware import token_required
expense_bp = Blueprint("expense_bp", __name__)


# ---------------------------------------------------------
# Create Expense
# ---------------------------------------------------------
@expense_bp.route("/expenses", methods=["POST"])
@token_required
def add_expense():

    payload = request.json

    response = create_expense(payload)

    return response


# ---------------------------------------------------------
# Get Expenses
# ---------------------------------------------------------
@expense_bp.route("/expenses", methods=["GET"])
@token_required
def expenses():

    user_id = request.args.get("user_id")

    response = get_expenses(user_id)

    return response


# ---------------------------------------------------------
# Update Expense
# ---------------------------------------------------------
@expense_bp.route(
    "/expenses/<document_id>",
    methods=["PUT"]
)
def edit_expense(document_id):

    payload = request.json

    response = update_expense(
        document_id,
        payload
    )

    return response


# ---------------------------------------------------------
# Delete Expense
# ---------------------------------------------------------
@expense_bp.route(
    "/expenses/<document_id>",
    methods=["DELETE"]
)
def remove_expense(document_id):

    response = delete_expense(document_id)

    return response
